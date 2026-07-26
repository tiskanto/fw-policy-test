# FW-Policy-Test Docker Image Creation
FROM python:3.14-slim-trixie

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends git
RUN apt-get install -y nmap sudo

WORKDIR /app

COPY requirements.txt /app
COPY tests /app/tests
COPY src /app/src
COPY data /app/data

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

ENTRYPOINT ["pytest"]
CMD ["-v" , "-s", "--tb=no"]
