# Machine-Learning-Based-Ransomware-Detection-with-Cuckoo-Sandbox-Graduation-Project
⚠️ WARNING: MALWARE-RELATED CONTENT
This repository contains scripts that interact with and download real ransomware samples from MalwareBazaar. These samples are for research and educational purposes only.

💀 These samples are extremely dangerous if mishandled.
❌ Do NOT run any scripts from this repository on personal or production systems.
✅ Always use a controlled, isolated virtual machine (e.g., VirtualBox or VMware) with:

No internet access

Shared folders disabled

Snapshots enabled

🛡️ The author is not responsible for any damage resulting from the misuse of this content.

📜 Script Descriptions
<details> <summary><strong>🔻 download_ransomware.sh</strong> – Download & extract real ransomware samples</summary>
📌 Description
This script automates the process of retrieving and extracting ransomware samples from MalwareBazaar using a specific tag.

🔧 What It Does
Queries the MalwareBazaar API for up to 500 ransomware samples.

Extracts their SHA256 hashes.

Downloads each sample as a ZIP file.

Extracts the payloads using the default password: infected.

Cleans up the ZIP archives after extraction.

🗂️ Filesystem Overview
perl
Copy code
~/Desktop/
├── ransomware_samples/     # Contains .zip archives of ransomware
├── extracted_samples/      # Contains the extracted (real) ransomware files
🧪 Usage
bash
Copy code
chmod +x download_ransomware.sh
./download_ransomware.sh
⚠️ Run this script only inside an isolated virtual machine!

</details>
<details> <summary><strong>🔻 extract_jsons.sh</strong> – Extract dynamic analysis JSON reports</summary>
📌 Description
This script collects .json report files from the nested reports/ folder inside each sample directory and consolidates them into a single folder for analysis.

🔧 What It Does
Creates a directory named all-json/.

Iterates through each sample folder.

Locates the .json file inside the reports/ subfolder.

Copies and renames the file to match the parent folder name (e.g., sample123.json).

🗂️ Example Folder Structure Before
python-repl
Copy code
samples/
├── sample1/
│   └── reports/
│       └── report.json
├── sample2/
│   └── reports/
│       └── analysis.json
...
🗂️ After Running the Script
python-repl
Copy code
all-json/
├── sample1.json
├── sample2.json
...
🧪 Usage
bash
Copy code
chmod +x extract_jsons.sh
./extract_jsons.sh
✅ Run this script from inside the directory containing all your sample folders.

</details>

