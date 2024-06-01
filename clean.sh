#!/bin/bash
cd react
npx prettier --write .
cd .. 
cd fastapi
black *.py
