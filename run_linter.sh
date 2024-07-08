#!/bin/bash
set -e

poetry run flake8 &
PID1=$!
poetry run mypy . &
PID2=$!

wait $PID1
wait $PID2
