# mkarakus2/sharing:airflow-v1.0.0
# https://github.com/airflow-helm/charts/blob/main/charts/airflow/docs/faq/configuration/extra-python-packages.md

FROM apache/airflow:2.2.5-python3.8

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
