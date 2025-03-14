FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p logs reports

CMD pytest -n4 && \
    mkdir -p logs_docker reports_docker && \
    mv logs/* logs_docker/ && \
    mv reports/* reports_docker/
