#!/bin/sh

echo "Starting the application with config at /etc/data/justlog.json"

# Ensure jq is installed
if ! command -v jq > /dev/null; then
  echo "jq not found, installing..."
  apk add --no-cache jq
fi

# Create logs folders
mkdir -p /etc/data/logs

# Check if justlog.json exists in /etc/data and MERGE_CHANNELS is set to 1
if [ -f /etc/data/justlog.json ] && [ "$MERGE_CHANNELS" = "1" ]; then
  echo "Merging channels fields from config.template.json to /etc/data/justlog.json"
  jq -s '.[0] * {channels: (.[0].channels + .[1].channels | unique)}' justlog.json /etc/data/justlog.json > /etc/data/justlog_merged.json
  mv /etc/data/justlog_merged.json /etc/data/justlog.json
else
  # Copy the config file if it doesn't exist or MERGE_CHANNELS is not set to 1
  cp justlog.json /etc/data/justlog.json
fi

# Start the application
exec ./app -config /etc/data/justlog.json
