#!/bin/bash

# Start the server
uvicorn app.main:app --host 0.0.0.0 --reload --port 8000 &
while true; do
    curl -v http://localhost:8000
    if [ $? -eq 0 ]; then
        # If connection successful, execute python test_data.py
        python test_data.py
        break
    fi
    sleep 0.1
done

while true; do
    sleep 600
done