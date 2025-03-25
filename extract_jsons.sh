#!/bin/bash
mkdir -p all-json
for d in */; do
  if [ -f "$d/reports/"*.json ]; then
    json_file=$(find "$d/reports/" -maxdepth 1 -name '*.json' | head -n 1)
    cp "$json_file" all-json/"${d%/}.json"
  fi
done

