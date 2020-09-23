#!/bin/bash
gunicorn -b 0.0.0.0:8080 -c config.py -e PYTHONBUFFERED=TRUE wsgi:application --log-file=-

