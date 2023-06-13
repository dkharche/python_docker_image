FROM python:alpine:3.17
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py