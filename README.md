# Week 01 — Cybersecurity Asset Inventory System

## Problem Statement
An organization maintains several IT assets such as computers, servers, routers, switches, and
software applications. Managing these assets manually makes it difficult to identify the assets,
track their security status, and determine which assets require immediate attention.

This project is a menu-driven Python CLI that lets a security administrator **add, search,
update, delete, and display** an organization's IT assets, with each asset classified by
**asset type**, **risk level**, and **security status**.

## Features
- Add a single asset or multiple assets in one session
- Search for an asset by Asset ID
- Update any field of an existing asset (leave blank to keep current value)
- Delete an asset (with confirmation prompt)
- Display all assets in a formatted report
- Security summary: total assets, counts by risk level, and counts by security status
- Input validation for Asset Type, Risk Level, and Security Status (only accepts valid categories)
- Duplicate Asset ID prevention
- Data persisted between runs in `data/assets.json`

## Data Fields
| Field | Description |
|---|---|
| Asset ID | Unique identifier for the asset |
| Asset Name | Descriptive name |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Network address of the asset |
| Operating System | OS running on the asset |
| Owner/Department | Owning team or department |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## Repository Structure
```
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py
├── data/
│   └── assets.json
├── tests/
│   └── test_cases.md
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
└── README.md
```

## How to Run
Requires Python 3.

```bash
cd src
python3 asset_inventory.py
```

Follow the on-screen menu (1–8) to add, search, update, delete, or display assets, or view the
security summary. All changes are automatically saved to `data/assets.json`.

## Sample Output
```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID       : A101
Asset Name     : HR-PC-01
Asset Type     : Workstation
IP Address     : 192.168.1.10
OS             : Windows 11
Department     : HR
Risk Level     : Medium
Status         : Secure
-----------------------------------------
Asset ID       : A102
Asset Name     : Web-Server
Asset Type     : Server
IP Address     : 192.168.1.20
OS             : Ubuntu
Department     : IT
Risk Level     : Critical
Status         : Vulnerable
-----------------------------------------
Asset ID       : A103
Asset Name     : Core-Router
Asset Type     : Router
IP Address     : 192.168.1.1
OS             : Cisco IOS
Department     : Network
Risk Level     : High
Status         : Warning
=========================================
Total Assets : 3
Critical Assets : 1
High Risk Assets : 1
Medium Risk Assets : 1
Vulnerable Assets : 1
=========================================
```

## Tests
See [`tests/test_cases.md`](tests/test_cases.md) for the full list of test cases covering add,
search, update, delete, display, validation, and persistence.

## Screenshots
The `screenshots/` folder contains images demonstrating each core operation (add, display,
search, update, delete, security summary, and input validation). Add your own screenshots there
before submitting, named to match the required repository structure.
