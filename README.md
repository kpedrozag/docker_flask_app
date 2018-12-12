# Deployment of an API built with Flask on a Ubuntu Xenial docker container

This project shows information about the deployment of an API built with Flask from a container of Ubuntu 16.04.

It is used a Dockerfile to build an image of Ubuntu Xenial where the requirements of the API are installed.

The API listen the requests through the port 5000

## How to deploy the API:

  1. Clone the repository: `$ git clone https://github.com/kpedrozag/docker_flask_app.git` and go to the directory `cd docker_flask_app`
  2. Build the docker image: `$ docker build -t flask_app:v1 .`
  3. Run an instance of the image: `$ docker run --name my_flask_app -p 5000:5000 -d flask_app:v1`
