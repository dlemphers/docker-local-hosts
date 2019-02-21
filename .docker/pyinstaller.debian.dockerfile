FROM python:latest

RUN apt-get update -y

RUN apt-get install -y \
    zlib1g-dev \
    libssl-dev \
    bash

ENV LD_LIBRARY_PATH /usr/local/lib

RUN pip install git+https://github.com/pyinstaller/pyinstaller
