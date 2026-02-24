FROM nikolaik/python-nodejs:python3.10-nodejs17

# Update and upgrade with retry mechanism
RUN apt-get update --fix-missing && \
    apt-get upgrade -y --fix-missing && \
    apt-get install ffmpeg -y --fix-missing

COPY . /app/
WORKDIR /app/

# Upgrade pip and install requirements
RUN pip3 install -U pip && \
    pip3 install -U -r requirements.txt

CMD python3 main.py
