const API_KEY = '254a20b0d98f4feaa63165439250511';
const BASE = 'https://api.weatherapi.com/v1/current.json';

const form = document.getElementById('searchForm');
const input = document.getElementById('locationInput');
const statusEl = document.getElementById('status');
const weatherEl = document.getElementById('weather');
const geoBtn = document.getElementById('geoBtn');

function setStatus(msg, isError = false) {
  statusEl.textContent = msg || '';
  statusEl.style.color = isError ? '#ffb4b4' : '';
}

function clearWeather() {
  weatherEl.innerHTML = '';
}

function iconUrl(url){
  if (!url) return '';
  if (url.startsWith('//')) return 'https:' + url;
  return url;
}

async function fetchWeather(query) {
  const url = `${BASE}?key=${API_KEY}&q=${encodeURIComponent(query)}&aqi=yes`;
  setStatus('Loading...');
  clearWeather();

  try {
    const res = await fetch(url);
    if (!res.ok) {
      const body = await res.text();
      throw new Error(`API error: ${res.status} ${body}`);
    }
    const data = await res.json();
    renderWeather(data);
    setStatus('');
  } catch (err) {
    console.error(err);
    setStatus('Could not fetch weather. Try a different location.', true);
  }
}

function renderWeather(data){
  if (!data || !data.location || !data.current) {
    setStatus('No data returned', true);
    return;
  }

  const loc = data.location;
  const cur = data.current;
  const icon = iconUrl(cur.condition.icon);

  weatherEl.innerHTML = `
    <div class="icon"><img alt="${cur.condition.text}" src="${icon}"></div>
    <div class="details">
      <div class="location">${loc.name}${loc.region ? ', ' + loc.region : ''} • ${loc.country} • local: ${loc.localtime}</div>
      <div class="temp">${Math.round(cur.temp_c)}°C <span style="font-size:0.6em;color:var(--muted)">/ ${Math.round(cur.temp_f)}°F</span></div>
      <div class="cond">${cur.condition.text}</div>
      <div class="meta">
        <div>Feels: ${Math.round(cur.feelslike_c)}°C</div>
        <div>Humidity: ${cur.humidity}%</div>
        <div>Wind: ${cur.wind_kph} kph</div>
        <div>Precip: ${cur.precip_mm} mm</div>
        <div>UV: ${cur.uv}</div>
      </div>
      ${renderAQI(cur.air_quality)}
    </div>
  `;
}

function renderAQI(aqi){
  if (!aqi) return '';
  const pm2_5 = typeof aqi['pm2_5'] === 'number' ? `PM2.5: ${aqi['pm2_5'].toFixed(2)}` : '';
  const pm10 = typeof aqi['pm10'] === 'number' ? `PM10: ${aqi['pm10'].toFixed(2)}` : '';
  const us_epa = aqi['us-epa-index'] ? `EPA index: ${aqi['us-epa-index']}` : '';
  const parts = [pm2_5, pm10, us_epa].filter(Boolean);
  return parts.length ? `<div class="meta" style="margin-top:8px;color:var(--muted)">${parts.join(' • ')}</div>` : '';
}

// handle form submit
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const q = input.value.trim();
  if (!q) {
    setStatus('Please enter a location', true);
    return;
  }
  setStatus('');
  clearWeather();
  fetchWeather(q);
});

// use geolocation
geoBtn.addEventListener('click', () => {
  if (!navigator.geolocation) {
    setStatus('Geolocation not supported by your browser', true);
    return;
  }
  setStatus('Getting your location...');
  clearWeather();

  navigator.geolocation.getCurrentPosition((pos) => {
    const q = `${pos.coords.latitude},${pos.coords.longitude}`;
    setStatus('');
    fetchWeather(q);
  }, (err) => {
    console.error(err);
    setStatus('Unable to get location', true);
  }, {timeout:10000});
});

// clear status when typing
input.addEventListener('input', () => setStatus(''));