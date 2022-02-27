FROM python:3.9.5-slim
ENV PYTHONBUFFERED 1
RUN apt update && apt install netcat -y
RUN mkdir /django
WORKDIR /django
COPY requirements.txt /django/
RUN pip3 install --user -r requirements.txt
COPY . /django/
RUN chmod +x ./startup.sh
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
CMD ./startup.sh
