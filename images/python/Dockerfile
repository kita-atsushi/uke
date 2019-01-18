FROM python:3.6

ARG proxy
ARG no_proxy

ENV http_proxy="${proxy}" \
    https_proxy="${proxy}" \
    HTTP_PROXY="${proxy}" \
    HTTPS_PROXY="${proxy}" \
    NO_PROXY="${no_proxy}" \
    no_proxy="${no_proxy}"

RUN mkdir /scripts
RUN mkdir /conf

COPY ./requirements.txt /
RUN pip install -r /requirements.txt
