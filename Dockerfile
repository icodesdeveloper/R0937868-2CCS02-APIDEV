FROM python:3.10.0-alpine
WORKDIR /code
RUN mkdir -p /code/db
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
