FROM python:2.7
ADD . /app
RUN pip install -r /app/requirements.txt
RUN pip install /app
