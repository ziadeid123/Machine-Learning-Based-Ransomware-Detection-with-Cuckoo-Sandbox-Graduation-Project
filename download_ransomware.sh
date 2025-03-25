#!/bin/bash

# Define the tag for ransomware and the number of samples to download
TAG="ransomware"  # Make sure this tag matches Windows ransomware samples
DOWNLOAD_LIMIT=500

# Determine OS
OS=$(uname -s)

# Download hash values from MalwareBazaar based on the tag
curl -XPOST -d "query=get_taginfo&tag=${TAG}&limit=${DOWNLOAD_LIMIT}" https://mb-api.abuse.ch/api/v1/ | grep sha256_hash | awk '{print $2}' > ${TAG}.raw

# OS Cleanup - Remove unwanted characters from the downloaded hash list
if [ ${OS} == Darwin ]; then
    sed -i.bak 's/\"//g' ${TAG}.raw
    rm ${TAG}.raw.bak
    sed -i.bak 's/\,//' ${TAG}.raw
    rm ${TAG}.raw.bak
elif [ ${OS} == Linux ]; then
    sed -i 's/\"//g' ${TAG}.raw
    sed -i 's/\,//' ${TAG}.raw
fi

# Rename the cleaned hash file
mv ${TAG}.raw ${TAG}.hash

# Create a directory for the downloaded ransomware samples
mkdir -p ~/Desktop/ransomware_samples

# Download the samples using their hash values
while read h; do
    curl -XPOST -d "query=get_file&sha256_hash=${h}" -o ~/Desktop/ransomware_samples/${h}.zip https://mb-api.abuse.ch/api/v1/
done < ${TAG}.hash

# Extract all ransomware samples using the password "infected"
mkdir -p ~/Desktop/extracted_samples
for file in ~/Desktop/ransomware_samples/*.zip; do
    7z e "$file" -p"infected" -o~/Desktop/extracted_samples/
done

# Cleanup - Remove zip archives after extraction
rm -rf ~/Desktop/ransomware_samples

echo "Download Complete, Files are in ~/Desktop/extracted_samples/"
