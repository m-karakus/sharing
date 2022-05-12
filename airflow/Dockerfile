# mkarakus2/sharing:airflow-v1.0.0
# https://github.com/coder2j/airflow-docker

FROM apache/airflow:slim-2.3.0-python3.10

COPY requirements.txt /requirements.txt

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
