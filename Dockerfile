# Use Ubuntu as the base image
FROM ubuntu:latest

# LABEL about the custom image
LABEL version="1.0"
LABEL maintainer="Tien Nguyen <tiennguyen047@gmail.com>"
LABEL description="This is a custom Docker Image for NCD project"

# Update Ubuntu Software repository
RUN apt-get update && \
    apt-get upgrade -y

# Update the package manager and install necessary dependencies
RUN apt-get install -y python3.11
RUN apt-get install -y python3-pip

# Install Flask
RUN pip3 install Flask

# Install ping package
RUN apt-get update && apt-get install -y iputils-ping

# Set current working dir
WORKDIR /usr/local/share

# create variable env PORT to import python
ENV PORT 5555

COPY microservice microservice

EXPOSE 2345

ENTRYPOINT [ "python3", "microservice/NCD_service/NCD_Adapter.py" ]