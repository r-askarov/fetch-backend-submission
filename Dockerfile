# Use the official Python 3.9.5 image as the base image
FROM python:3.9.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

EXPOSE 8000

CMD ["python", "src/backend.py"]
