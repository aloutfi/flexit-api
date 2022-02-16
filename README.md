# flexit-api

![platform-version](https://img.shields.io/badge/python-3.10.2-1666a9)
![formatter](https://img.shields.io/badge/formatter-Black-000000)
![flexit-service-ci](https://github.com/aloutfi/flexit/actions/workflows/flexit-ci.yml/badge.svg)


This is the presentation layer for flexit. It is implemented with FastAPI.


During installation, the [flexit package](https://github.com/aloutfi/flexit) is installed via `requirements.txt`
## Usage
Assuming you have access to a database as described in the ADR, this system can be ran via docker-compose or in a virtual environment.

### Docker-Compose strategy:
```bash
docker-compose up
```


### Virtual Environment strategy:
```bash
python -m venv && source venv/bin/activate && pip install -r requirements.txt

export DATABASE_URL='<your_db_url>'

uvicorn app.main:app --reload
```