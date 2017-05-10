FROM python:2.7
RUN apt-get -y update && apt-get -y install libev-dev
ADD . /app
RUN pip install -r /app/requirements.txt
RUN pip install /app
