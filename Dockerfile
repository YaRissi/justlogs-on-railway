FROM ghcr.io/gempir/justlog:latest

ARG ADMINS ADMINAPIKEY USERNAME OAUTHTOKENFORCHAT BOTVERIFIED MYTWITCHCLIENTID MYSECRETCLIENTID CHANNELS LOGLEVEL

USER root

RUN apk add --no-cache python3 py3-pip 

COPY config.template.json config.template.json
COPY scripts/convert_args.py convert_args.py
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN python3 convert_args.py --input config.template.json --output justlog.json

HEALTHCHECK CMD curl --fail http://localhost:8025 || exit 1

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]