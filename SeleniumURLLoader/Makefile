# Makefile

# Docker image name
IMAGE_NAME=my-python-app

# URL to pass to the app
URL=https://ann.inc/

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container with URL argument
run:
	docker run --platform linux/amd64 -p 4000:80 $(IMAGE_NAME) 

# Build and run the Docker container
all: build run