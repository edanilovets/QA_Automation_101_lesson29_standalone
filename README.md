# Build the docker image with chrome and chromedriver (doens't work)
### Build and check the docker image
docker build -t selenium-tests:latest .

docker run --rm -it selenium-tests bash
chromium --version
chromedriver --version
chromium --headless --no-sandbox --disable-dev-shm-usage --disable-setuid-sandbox --remote-debugging-port=9222

### Run the tests
docker run --rm selenium-tests:latest

### Run the tests with a shared memory of 2GB
docker run --rm --shm-size=2g selenium-tests


# Create a smoke test container
docker build -t smoke-test:latest .
docker run --rm smoke-test:latest

# Using selenium/standalone-chrome
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest