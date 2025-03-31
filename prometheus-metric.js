const express = require('express');
const promBundle = require('express-prom-bundle');

const app = express();
const metricsMiddleware = promBundle({
  includeMethod: true,
  includePath: true,
  normalizePath: [['^/api/v1/.*', '/api/v1/#param']],
  metricsPath: '/metrics',
});

app.use(metricsMiddleware);

app.get('/api/endpoint', (req, res) => {
  // Your endpoint logic
  res.json({ status: 'ok' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});