FROM python:3.8

WORKDIR /app
COPY . .

run pip install -r requirements.txt

ENTRYPOINT ["python"]
EXPOSE 5000
EXPOSE 8080
CMD ["app.py"]

