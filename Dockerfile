FROM python:3.10

WORKDIR /main
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]