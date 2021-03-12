#!/bin/bash

# sleep 35

alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8080
