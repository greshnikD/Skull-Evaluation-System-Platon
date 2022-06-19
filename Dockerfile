FROM python:3
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
COPY gmed_project/ /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
