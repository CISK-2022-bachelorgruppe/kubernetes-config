FROM python:3.9.5-slim
RUN mkdir /python
WORKDIR /python
COPY req.py .
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt
CMD python3 req.py