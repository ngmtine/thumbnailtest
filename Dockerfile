FROM python:3
USER root

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /root/src
COPY ./src/main.py /root/src
WORKDIR /root/src

# RUN apt install -y AtomicParsley ffmpeg
RUN pip install youtube-dl
