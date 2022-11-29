FROM python:3.11-slim-buster

WORKDIR /python-docker

RUN sudo apt-get install -y chromium-browser 

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", '--port', '$PORT']