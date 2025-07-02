FROM python:alpine

WORKDIR /school-enrollment

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["sh", "-c", "alembic upgrade head && python api/server.py"]