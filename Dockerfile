FROM python:3.10-slim

# Install system dependencies and set timezone
RUN apt-get update -y && \
    apt-get install -y ffmpeg tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Singapore /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD python main.py
