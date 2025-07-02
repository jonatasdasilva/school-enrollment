FROM python:alpine

WORKDIR /school-enrollment

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN alembic upgrade head
RUN chown -R 1000:1000 postgres_data

CMD ["python", "api/server.py"]