#!/usr/bin/bash

cd /home/maxim/Desktop/putoran/
#source venv/bin/activate

echo "Hello, World!"

source venv/bin/activate


uvicorn main:app --reload --port 8000 --host 127.0.0.1
