# Delinquent Text File Processing

## Description

This repository contains scripts to process a delinquent text file, extract relevant information, and check the reachability of listed IPs.

## Scripts

1. **get_full_info_delinquent.py**: Python script to parse the delinquent text file and generate `common.xlsx` containing matched data based on required public IPs.

2. **ping_delinquent.py**: Python script to ping the IPs listed in `common.xlsx` and categorize them into reachable and unreachable IPs. Generates `reachable.xlsx` and `unreachable.xlsx`.

## Instructions

### Requirements

- Python 3.x
- Dependencies: `openpyxl`, `tqdm`

### Steps

1. **Filter the Delinquent Text File**:
   - Ensure the delinquent text file is parsed correctly to extract necessary information.

2. **Set Path in Command Prompt**:
   - Open Command Prompt (CMD) and navigate to the directory where scripts and filtered files are stored using `cd`.

3. **Generate Common Data**:
   - Execute `python get_full_info_delinquent.py` to generate `common.xlsx`.
   - Install `openpyxl` using `pip install openpyxl` if not already installed.

4. **Check Reachability**:
   - After `common.xlsx` is generated, execute `python ping_delinquent.py` to check the reachability of IPs.
   - Install `tqdm` using `pip install tqdm` if not already installed.

5. **Output Files**:
   - `reachable.xlsx`: Contains reachable IPs.
   - `unreachable.xlsx`: Contains unreachable IPs.

## Author

- Your Name
- Contact Information
