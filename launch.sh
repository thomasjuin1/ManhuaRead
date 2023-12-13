#!/bin/bash

# Check if the mongo-express container is running
if [ "$(docker ps -q -f name=mongo-express)" ]; then
    echo "mongo-express container is already running"
else
    # If not running, start the mongo-express container in detached mode
    docker compose up -d mongo-express
fi

# Build and start the api container
docker compose down api
docker compose up --build api