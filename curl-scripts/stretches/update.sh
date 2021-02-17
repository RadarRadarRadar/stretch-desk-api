#!/bin/bash

curl "http://localhost:8000/stretch/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "stretch": {
      "name": "'"${NAME}"'",
      "description": "'"${DESCRIPTION}"'",
      "video": "'"${VIDEO}"'",
      "instructions": "'"${INSTRUCTIONS}"'"
    }
  }'

echo
