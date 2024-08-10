FROM python:3.9

WORKDIR /krisp_assignment

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]