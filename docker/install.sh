#!/bin/bash

apt-get update -yq
apt-get install -yq python3-pip libpq-dev postgresql-client

pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput