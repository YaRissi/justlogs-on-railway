FROM ghcr.io/gempir/justlog:latest

ARG admins adminAPIKey username oauthtokenforchat botVerified mytwitchclientid myscretclientid channels

USER root

RUN apk add --no-cache python3 py3-pip \
  && mkdir -p /data/logs 

COPY config.template.json /etc/config.template.json
COPY scripts/convert_args.py convert_args.py

RUN  python3 convert_args.py --input /etc/config.template.json --output /etc/justlog.json

RUN cat /etc/justlog.json


HEALTHCHECK CMD curl --fail http://localhost:8025 || exit 1

#EXPOSE 8025