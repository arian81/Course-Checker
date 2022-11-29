FROM browserless/chrome
FROM python:3.11-slim-buster

WORKDIR /python-docker

# RUN apt-get update && apt-get install -y chromium-browser 

COPY . .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["python3", "main.py"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", '--port', '$PORT']