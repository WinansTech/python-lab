#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests

response = requests.get("https://httpbin.org/json")
print(response.json())