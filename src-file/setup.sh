#!/bin/bash

docker build --tag src-file .
docker run --env API_K -ti src-file