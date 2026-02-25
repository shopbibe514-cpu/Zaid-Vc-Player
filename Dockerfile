FROM nikolaik/python-nodejs:python3.10-nodejs18

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set timezone
ENV TZ=Asia/Singapore
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYROGRAM_SYNC_TIME=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["python", "main.py"]
