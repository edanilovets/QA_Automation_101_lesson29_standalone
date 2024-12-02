# Build the docker image with chrome and chromedriver
## Solution at the end
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

# Create a smoke test container
```bash
docker build -t smoke-test:latest .
docker run --rm smoke-test:latest
```

# Using selenium/standalone-chrome
```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
```


# Run tests locally
```bash
pytest --headless
pytest --headless --html=local_reports/report.html --self-contained-html
```
