ARG COMMON_PATH
ARG OS_NAME
ARG OS_VERSION
ARG PORT_PRIVATE
ARG PORT_EXPOSE
ARG PY_SITE_PACKAGES

# Use Ubuntu as the base image
FROM ${OS_NAME}:${OS_VERSION}

# LABEL about the custom image
LABEL version="1.0"
LABEL maintainer="Tien Nguyen <tiennguyen047@gmail.com>"
LABEL description="This is a custom Docker Image for NCD project"

# Set current working dir
WORKDIR /usr/local/share

# create variable env PORT to import python
ENV PORT=8080

# # copy microservice folder to container
COPY microservice ./microservice
COPY build/package_requirements.txt ./

# COPY microservice build/package_requirements.txt ./

# Update Ubuntu Software repository
RUN apt-get update && \
    apt-get upgrade -y && \
    # Update the package manager and install necessary dependencies
    apt-get install -y python3.11 && \
    apt-get install -y python3-pip && \
    # Install ping package
    apt-get update && apt-get install -y iputils-ping && \
    mkdir log_controler && \
    pip3 install --no-cache-dir -r package_requirements.txt

# Expose port 2345 to local host
EXPOSE 2345

# Run command line when start container
ENTRYPOINT ["python3", "microservice/NCD_service/NCD_Adapter.py"]