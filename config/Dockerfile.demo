# Use an official Python image
FROM python:3.10-slim

# Copy project files into the container
WORKDIR /app
COPY . /app

# Set environment variables for Chrome
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the tests
CMD ["pytest",  "-m", "smoke"]
