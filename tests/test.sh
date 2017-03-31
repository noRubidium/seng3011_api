#!/usr/bin/env bash

export URL_VERSION='http://127.0.0.1:8000/v2/'
npm install
../node_modules/jasmine-node/bin/jasmine-node .
