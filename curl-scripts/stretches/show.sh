#!/bin/bash

curl "http://localhost:8000/stretch/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
