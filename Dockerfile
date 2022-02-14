FROM python:3.10.2

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./dist /code/dist

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]