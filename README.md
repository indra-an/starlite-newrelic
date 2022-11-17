# starlite-newrelic
Starlite Newrelic

## Requirements
- Python 3.10
- [Poetry](https://python-poetry.org/)


## Running
```
poetry install
NEW_RELIC_CONFIG_FILE=newrelic.ini poetry run newrelic-admin run-program uvicorn --port 8080 app:app
```
