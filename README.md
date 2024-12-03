# Build the docker image with chrome and chromedriver
### Solution at the end of the tread
https://gist.github.com/varyonic/dea40abcf3dd891d204ef235c6e8dd79

### Build and check the docker image
```bash
docker build -t ui-tests:latest -f Dockerfile.chrome .
```

### Debug the docker image
```bash
docker run --rm -it ui-tests bash
```

### Run the tests
```bash
docker run --rm ui-tests:latest
docker run --rm -v $(pwd)/docker_reports:/app/docker_reports ui-tests:latest
```


### Run the tests with a shared memory of 2GB
```bash
docker run --rm --shm-size=2g ui-tests
```

# Using selenium/standalone-chrome
```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
```

# Jenkins Freestyle job: Smoke Docker UI tests
```bash
/usr/local/bin/docker build -t ui-tests-job:latest -f config/Dockerfile.chrome .
/usr/local/bin/docker run --rm ui-tests-job:latest
```

# Jenkins Freestyle job: Smoke Local UI tests
### First stage
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Second stage
```bash
#!/bin/bash
source venv/bin/activate
# Check if the HEADLESS parameter is true
if [ "$HEADLESS" = "true" ]; then
    echo "Running in headless mode..."
    pytest -m smoke --headless --env $ENV
else
    echo "Running in normal mode..."
    pytest -m smoke --env $ENV
fi
```

# Jenkins Pipeline job: Regression Local UI tests
```bash
# config/pipeline-regression-ui
```