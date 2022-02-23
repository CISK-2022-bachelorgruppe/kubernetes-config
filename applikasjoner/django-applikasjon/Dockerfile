FROM python:3.9.5-slim
ENV PYTHONBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django/
RUN pip3 install --user -r requirements.txt
COPY . /django/
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000
