# FROM python:3.13
#
# WORKDIR /app
#
# COPY requirements.txt ./
# COPY pytest.ini ./
# COPY config.py ./
# COPY .env ./
#
# COPY tests/ ./tests/
# COPY api/ ./api/
# COPY fixtures/ ./fixtures/
#
# RUN pip install --no-cache-dir -r requirements.txt
#
# RUN mkdir -p logs reports
#
# CMD pytest tests/ -n auto --html=reports/report.html --self-contained-html | tee logs/test_logs.log