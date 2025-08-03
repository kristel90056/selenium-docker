FROM python:3.10-slim

WORKDIR /app
COPY test_script.py .

RUN pip install selenium

CMD ["python", "test_script.py"]
