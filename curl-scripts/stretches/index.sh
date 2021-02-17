#!/bin/bash

curl "http://localhost:8000/stretches/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
