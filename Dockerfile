FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir pandas numpy
CMD [ "python", "python_etl/etl_to_sqlite.py" ]
