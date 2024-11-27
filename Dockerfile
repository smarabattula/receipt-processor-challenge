FROM python:3.13.0a6-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="/app/.venv/bin:$PATH"

COPY receipt_processor /app/receipt_processor
COPY app.py /app/app.py
COPY api.yml /app/api.yml

EXPOSE 1777

CMD ["python", "app.py"]
