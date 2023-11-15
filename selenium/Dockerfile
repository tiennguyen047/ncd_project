ARG OS_NAME
ARG OS_VERSION
ARG W_DIR
# Use Ubuntu as the base image
FROM ${OS_NAME}:${OS_VERSION}

# Set current working dir
WORKDIR /usr/local/share

COPY driver/chromedriver .
COPY driver/chrome_114_amd64.deb .
COPY selenium_code.py .

# Update the package manager and install necessary dependencies
# Update Ubuntu Software repository
RUN apt-get update && \
    apt-get install -y python3.11 && \
    apt-get install -y python3-pip && \
    apt-get install -y wget && \
    pip install selenium && \
    cat /etc/os-release

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN apt-get install -f -y /usr/local/share/chrome_114_amd64.deb && \
    rm /usr/local/share/chrome_114_amd64.deb && \
    echo "Chrome: " && google-chrome --version
