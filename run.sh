#!/usr/bin/env bash

if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

pytest --alluredir=allure-results
chmod -R 777 ./allure-results
