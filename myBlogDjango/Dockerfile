FROM python:3.5.2

LABEL maintainer="duogelingyu <AlbertLearnEmail@163.com>"

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 80 

CMD ["python", "manager.py","runserver 0.0.0.0:"]