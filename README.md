# files-microservice
[![Build Status](https://travis-ci.org/devopsicon/files-microservice.svg?branch=develop)](https://travis-ci.org/devopsicon/files-microservice)
[![Maintainability](https://api.codeclimate.com/v1/badges/ee91316741bd604fa06f/maintainability)](https://codeclimate.com/github/devopsicon/files-microservice/maintainability)
<a href="https://codeclimate.com/github/devopsicon/files-microservice/test_coverage"><img src="https://api.codeclimate.com/v1/badges/ee91316741bd604fa06f/test_coverage" /></a>
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Docker Repository on Quay](https://quay.io/repository/devopsicon/filesmicroservice/status "Docker Repository on Quay")](https://quay.io/repository/devopsicon/filesmicroservice)

Files Microservice
Files service is developed using Tornado framework of Python language, which is designed for extreme high performance asynchronous operation which is ideal for 
an async activity such as file saving.

In the future this microservice will use a database to save file binaries, currently it is saving on the deployed folder within the docker image.

## Testing locations
* [Unit and Integration](unit_test.py)

## DevOps Automation Notes
* TravisCI configuration is via .travis.yml file
* Docker configuration is via Dockerfile

## Contribution Notes
1. This project uses Python and Tornado
2. All tests must be done as pre-merged checks
3. master and development branches is protected and only way to contribute is via Pull-Request
4. Unit and Integration testing coverage is monited via CodeClimate 

