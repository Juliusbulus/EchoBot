#!/bin/bash

# Server Media Directory Setup Script for EchoBot
# This script should be run on the server (e.g., via GitLab CI) to prepare the unified media structure.

set -e

# --- Configuration ---
# Default host path for the media directory if not specified in .env
DEFAULT_MEDIA_HOST_DIR="/home/wotori/echobot/media"

# Find the project root directory (the parent of the 'scripts' directory)
PROJECT_ROOT=$(dirname "$0")/..

# Path to the .env file in the project root
ENV_FILE="$PROJECT_ROOT/.env"

# Read MEDIA_HOST_DIR from .env file if it exists
if [ -f "$ENV_FILE" ]; then
    # Use grep to find the line and cut to get the value after '='
    # Also remove potential carriage returns (^M) from Windows-edited .env files
    MEDIA_HOST_DIR=$(grep '^MEDIA_HOST_DIR=' "$ENV_FILE" | cut -d '=' -f2- | tr -d '[:space:]')
    echo "📄 Found MEDIA_HOST_DIR in .env file: $MEDIA_HOST_DIR"
fi

# Use the default value if MEDIA_HOST_DIR is not set in the .env file
MEDIA_HOST_DIR="${MEDIA_HOST_DIR:-$DEFAULT_MEDIA_HOST_DIR}"


echo "🎵 Setting up unified media structure on server..."
echo "Host directory: $MEDIA_HOST_DIR"

# Create the main media directory.
# The application running inside Docker will create the necessary subdirectories.
echo "📁 Creating main media directory..."
mkdir -p "$MEDIA_HOST_DIR"

# Set appropriate permissions for the top-level directory.
echo "🔐 Setting permissions for $MEDIA_HOST_DIR..."
chmod 755 "$MEDIA_HOST_DIR"

# Create a placeholder file to ensure the directory is tracked by Git if empty.
touch "$MEDIA_HOST_DIR/.keep"

echo ""
echo "✅ Server media directory created successfully!"
echo ""
echo "The application will create the following structure inside $MEDIA_HOST_DIR as needed:"
echo "  ├── news/"
echo "  ├── voice/generated_audio/"
echo "  ├── music/soundcloud_songs/"
echo "  ├── music/google_drive_songs/"
echo "  ├── music/suno_songs/"
echo "  ├── state/"
echo "  ├── memory/"
echo "  └── videos/"
echo ""
echo "Next steps:"
echo "1. Ensure your .env file on the server sets MEDIA_HOST_DIR=\"$MEDIA_HOST_DIR\""
echo "2. Run 'docker-compose up -d --build' to start the application."
echo ""
echo "To verify the setup, run:"
echo "  ls -la $MEDIA_HOST_DIR/"
