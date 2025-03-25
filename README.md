⚠️ Malware-Related Warning
⚠️ WARNING: MALWARE-RELATED CONTENT
This repository contains scripts that download and handle real ransomware samples from MalwareBazaar for educational and research purposes only.

🧪 Always use an isolated virtual machine with:

- No internet access

- Snapshots enabled

- Shared folders disabled

💀 Mishandling may harm your system.
🛡️ The author assumes no responsibility for misuse.

📜 Script Descriptions
<details> <summary><strong>🔻 download_ransomware.sh</strong> – Download & Extract Ransomware Samples</summary>
📌 Description
This script automates the process of downloading ransomware samples from MalwareBazaar based on the "ransomware" tag and extracts them from password-protected ZIP archives.

🔧 What It Does
Queries MalwareBazaar for up to 500 ransomware samples.

Extracts their SHA256 hashes from the API response.

Downloads the samples as ZIP files.

Extracts the contents using the password infected.

Deletes the ZIP files after extraction.

🗂️ Filesystem Overview

~/Desktop/
├── ransomware_samples/      # Contains .zip ransomware files
└── extracted_samples/       # Contains extracted (real) ransomware executables
▶️ Usage

chmod +x download_ransomware.sh
./download_ransomware.sh
⚠️ Run only inside a sandboxed virtual machine.

</details>
<details> <summary><strong>🔻 extract_jsons.sh</strong> – Collect Dynamic Analysis JSON Reports</summary>
📌 Description
This script collects .json reports from individual reports/ subfolders inside each sample directory and consolidates them into one folder for ML processing or manual review.

🔧 What It Does
Creates a folder named all-json/.

Iterates through each sample directory.

Finds the first .json file inside reports/.

Copies and renames it as sample-name.json into all-json/.

🗂️ Example Folder Structure
Before Running:


samples/
├── sample1/
│   └── reports/
│       └── report.json
├── sample2/
│   └── reports/
│       └── analysis.json
After Running:


all-json/
├── sample1.json
├── sample2.json
▶️ Usage

chmod +x extract_jsons.sh
./extract_jsons.sh
✅ Run this script from inside the folder that contains all your sample directories.

</details>
