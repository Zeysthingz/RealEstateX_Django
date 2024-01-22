#pull official base image
FROM python:3.10-slim-buster

RUN apt-get update

RUN apt-get install -y python3-dev build-essential

#set enviroment veriables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv


# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv


#our python is under venv/bin location
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#copy all project under linux /srv/app root
COPY . /srv/app
WORKDIR /srv/app




