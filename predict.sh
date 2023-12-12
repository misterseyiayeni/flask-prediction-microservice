#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "n_samples": '"$1"'
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict | grep prediction