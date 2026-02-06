#!/bin/bash

# SoundCloud Token Exchange Script
# Usage: ./get_soundcloud_token.sh YOUR_AUTHORIZATION_CODE

if [ -z "$1" ]; then
    echo "Usage: $0 YOUR_AUTHORIZATION_CODE"
    echo ""
    echo "First, get an authorization code by visiting:"
    echo "https://soundcloud.com/connect?client_id=kvBp5F5Y7o3uFEkKJyO51q1wF7VqZrdk&redirect_uri=http://localhost&response_type=code"
    echo ""
    echo "After authorizing, copy the 'code' parameter from the redirect URL"
    exit 1
fi

AUTHORIZATION_CODE="$1"
CLIENT_ID="kvBp5F5Y7o3uFEkKJyO51q1wF7VqZrdk"
CLIENT_SECRET="hrvpfqKXKImPrVmAaSec2slkQAgp12LI"
REDIRECT_URI="http://localhost"

echo "Exchanging authorization code for tokens..."
echo "Code (first 20 chars): ${AUTHORIZATION_CODE:0:20}..."

RESPONSE=$(curl -s -X POST "https://api.soundcloud.com/oauth2/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "client_id=${CLIENT_ID}" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "redirect_uri=${REDIRECT_URI}" \
  -d "code=${AUTHORIZATION_CODE}")

echo ""
echo "Response:"
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

# Extract tokens if successful
ACCESS_TOKEN=$(echo "$RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('access_token', ''))" 2>/dev/null)
REFRESH_TOKEN=$(echo "$RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('refresh_token', ''))" 2>/dev/null)

if [ -n "$ACCESS_TOKEN" ]; then
    echo ""
    echo "=========================================="
    echo "✅ SUCCESS! Add these to your .env file:"
    echo "=========================================="
    echo ""
    echo "SOUNDCLOUD_CLIENT_ID=${CLIENT_ID}"
    echo "SOUNDCLOUD_CLIENT_SECRET=${CLIENT_SECRET}"
    echo "SOUNDCLOUD_ACCESS_TOKEN=${ACCESS_TOKEN}"
    if [ -n "$REFRESH_TOKEN" ]; then
        echo "SOUNDCLOUD_REFRESH_TOKEN=${REFRESH_TOKEN}"
    fi
    echo ""
else
    echo ""
    echo "❌ Failed to get tokens. Check the error message above."
fi

