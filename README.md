# fake-users-agents
Python module for render fake users agents


```python
from user_agents.client import UserAgent
client = UserAgent()
client.random()
```

```json
{
    "appName": "Netscape",
    "connection": {
      "downlink": 10,
      "effectiveType": "4g",
      "rtt": 50
    },
    "platform": "Win32",
    "pluginsLength": 3,
    "vendor": "Google Inc.",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "viewportHeight": 970,
    "viewportWidth": 1900,
    "deviceCategory": "desktop",
    "screenHeight": 1080,
    "screenWidth": 1920,
    "weight": 0.0007918803225303125
}
```
