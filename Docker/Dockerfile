FROM python:3.10-slim


RUN apt-get update \
  && apt-get -y install wget ghostscript tesseract-ocr tesseract-ocr-rus djvulibre-bin 

WORKDIR /tmp