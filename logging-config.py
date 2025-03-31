import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger('api')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage:
logger.info('API request', extra={
    'method': 'GET',
    'endpoint': '/api/data',
    'duration_ms': 45,
    'user_id': 'abc123'
})