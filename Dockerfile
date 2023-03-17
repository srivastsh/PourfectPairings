FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

# Install 'gcc' and 'build-essential' packages, then install Python packages from 'requirements.txt'
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential && \
    pip install -r requirements.txt && \
    apt-get purge -y --auto-remove gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0", "--server.port", "8080"]
