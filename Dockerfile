FROM python:3.8

WORKDIR /usr/src/myapp

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "app:app"]