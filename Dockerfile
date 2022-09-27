FROM "debian:8"

LABEL maintainer="Michel Peterson \
      <michel.peterson@l1nuxc0d3.com>"


ADD ./sourceconf/ /piwik-tools/

RUN apt-get update && \
    apt-get -y install python-dev libcurl4-openssl-dev libssl-dev python-pip && \
    pip install pycurl==7.43.0.5 xmltodict && \
    apt-get clean

WORKDIR /piwik-tools
