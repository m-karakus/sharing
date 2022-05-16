# mkarakus2/sharing:airflow-v1.0.0
# https://github.com/coder2j/airflow-docker

FROM apache/airflow:slim-latest-python3.10

COPY requirements.txt /requirements.txt 
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r /requirements.txt
