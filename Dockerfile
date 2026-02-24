FROM python:3.10-slim

# Install everything needed
RUN apt-get update -y && \
    apt-get install -y ffmpeg tzdata ntpdate inetutils-tools && \
    # Force time sync multiple times
    ntpdate -u pool.ntp.org || true && \
    ntpdate -u time.google.com || true && \
    ntpdate -u time.facebook.com || true && \
    # Set timezone to UTC
    ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV TZ=UTC
ENV PYTHONUNBUFFERED=1
ENV PYROGRAM_SYNC_TIME=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["python", "main.py"]
