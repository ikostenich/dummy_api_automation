#!/usr/bin/bash

source ./env.sh

docker run \
-e APP_ID=$APP_ID \
dummy_api_automation \
/bin/bash -c pytest