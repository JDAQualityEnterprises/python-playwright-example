# Basic python playwright tests
Demonstrating...
* Page object
* Logger used in page objects
* Model objects (POPO) used for domain data
* html report 

# Running tests from the container
* Build the image:
  * docker build -t example-playwright-docker .
* Run the tests in the container:
  * docker run -it -e secrets.env example-playwright-docker