FROM python:3.10.2

LABEL MAINTAINER="Christopher Mickelle cm._13@live.com"

WORKDIR /Code

COPY . /Code

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]