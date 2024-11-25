# Use Python 3.11.7 slim as the base image
FROM python:3.11.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the lesson28 directory into the container
COPY . /app

# Add the `src` directory to the Python path
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Install system dependencies for Selenium
RUN apt-get update \
    && apt-get install -y wget gnupg unzip curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome and ChromeDriver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/`curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose any required ports (if needed)
EXPOSE 4444

# Define the entry point for running tests
CMD ["pytest", "tests"]
