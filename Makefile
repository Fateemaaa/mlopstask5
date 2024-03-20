.PHONY: build run

build:
    docker build -t python:3.9-slim .

run:
    docker run -p 5000:5000 python:3.9-slim
