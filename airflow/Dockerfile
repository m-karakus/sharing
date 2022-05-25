# mkarakus2/sharing:airflow-v1.0.0
# https://github.com/coder2j/airflow-docker

# FROM apache/airflow:slim-latest-python3.10
FROM apache/airflow:2.2.4

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# docker build . --tag mkarakus2/sharing:airflow-v1.0.0 
# docker push mkarakus2/sharing:airflow-v1.0.0