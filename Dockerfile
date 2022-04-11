FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requerements.txt .

RUN pip install -r requerements.txt

COPY . .


EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]