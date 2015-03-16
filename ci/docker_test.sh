#!/bin/bash
#
# Usage: docker_test.sh [DOCKER_IP]

set -e

DOCKER_IP="$1"
export SUPERUSER_NAME=minicomi
export SUPERUSER_PASSWORD=minicomi
export SUPERUSER_EMAIL='minicomi+test@joefriedl.net'

if [ -z "$DOCKER_IP" ]; then
    DOCKER_IP='127.0.0.1'
fi

export MINICOMI_BASE_URL="http://$DOCKER_IP:5000"

behave -t ~@local
