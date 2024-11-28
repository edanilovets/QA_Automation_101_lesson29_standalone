# Build the docker image with chrome and chromedriver
## Solution at the end
https://gist.github.com/varyonic/dea40abcf3dd891d204ef235c6e8dd79

### Build and check the docker image
```bash
docker build -t selenium-tests:latest .
```

### Debug the docker image
```bash
docker run --rm -it selenium-tests bash
```

### Run the tests
```bash
docker run --rm selenium-tests:latest
docker run --rm -v $(pwd)/docker_reports:/app/docker_reports selenium-tests:latest
```


### Run the tests with a shared memory of 2GB
```bash
docker run --rm --shm-size=2g selenium-tests
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


# Allure Command-Line Tool Examples

### Generate Allure Report
```bash
allure generate -c -o ./reports/my-custom-report ./allure-results
allure generate --single-file
```

### Serve Allure Report
```bash
allure serve -p 8080 ./allure-results
```

### Open Existing Report
```bash
allure open -p 9090 -h localhost ./reports/my-custom-report
```

### Display Installed Plugins
```bash
allure plugin
```

### Advanced Options
- **Custom Config:**
  ```bash
  allure generate --config ./custom-allure-config.yaml ./allure-results
  ```
- **Report Language:**
  ```bash
  allure generate --lang en ./allure-results
  ```
- **Report Name:**
  ```bash
  allure generate --name "My Test Report" ./allure-results

