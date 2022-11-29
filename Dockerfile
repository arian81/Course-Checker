# FROM browserless/chrome
# FROM python:3.11-slim-buster
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive


WORKDIR /python-docker

RUN apt-get update && apt-get install -y gcc make chromium-browser python3 python3-dev python3-distutils python3-pip
RUN apt-get update && apt-get install chromium-chromedriver -y

COPY . .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["python3", "main.py"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", '--port', '$PORT']