FROM ubuntu:22.04

LABEL version=1.0.0
LABEL maintainer="Diptonil Roy"

WORKDIR /app

ADD chasse /bin/chasse
COPY src /app/src

ENV PATH "$PATH:/bin/chasse"
