# Test Cases — Cybersecurity Asset Inventory System

| # | Test Case | Input | Expected Output | Status |
|---|-----------|-------|------------------|--------|
| 1 | Add a single valid asset | Asset ID `A104`, Name `Finance-PC`, Type `Workstation`, IP `192.168.1.40`, OS `Windows 10`, Dept `Finance`, Risk `Low`, Status `Secure` | Asset added and saved to `data/assets.json` | Pass |
| 2 | Add asset with duplicate Asset ID | Asset ID `A101` (already exists) | Program rejects the ID and re-prompts for a unique one | Pass |
| 3 | Add asset with invalid Asset Type | Type `Laptop` | Program rejects input and re-prompts until a valid type (Workstation/Server/Router/Switch/Application) is given | Pass |
| 4 | Add asset with invalid Risk Level | Risk `Extreme` | Program rejects input and re-prompts until Low/Medium/High/Critical is given | Pass |
| 5 | Add multiple assets in one session | Enter number of assets: 3, then details for each | All 3 assets added sequentially and saved | Pass |
| 6 | Search for an existing asset | Asset ID `A102` | Full asset details for Web-Server printed | Pass |
| 7 | Search for a non-existent asset | Asset ID `X999` | "No asset found with ID 'X999'." | Pass |
| 8 | Update an existing asset's Risk Level | Asset ID `A103`, new Risk Level `Critical`, other fields blank | Only Risk Level changes; all other fields unchanged; change persisted | Pass |
| 9 | Update a non-existent asset | Asset ID `X999` | "No asset found with ID 'X999'." | Pass |
| 10 | Delete an existing asset (confirmed) | Asset ID `A101`, confirm `y` | Asset removed from list and from `data/assets.json` | Pass |
| 11 | Delete an existing asset (cancelled) | Asset ID `A101`, confirm `n` | Asset remains unchanged | Pass |
| 12 | Delete a non-existent asset | Asset ID `X999` | "No asset found with ID 'X999'." | Pass |
| 13 | Display all assets | Menu option 6 with 3 assets loaded | Formatted report with `=====` header, each asset separated by `-----`, and summary counts at the bottom | Pass |
| 14 | Security summary counts | 3 assets: 1 Critical/Vulnerable, 1 High/Warning, 1 Medium/Secure | Total Assets: 3, Critical Assets: 1, High Risk Assets: 1, Medium Risk Assets: 1, Vulnerable Assets: 1 | Pass |
| 15 | Display with zero assets | Empty `data/assets.json` | "No assets found." message instead of a crash | Pass |
| 16 | Empty required field on Add | Blank Asset Name | Program re-prompts and refuses to accept an empty value | Pass |
| 17 | Persistence across runs | Add an asset, exit, relaunch program, display assets | Newly added asset is present after restart (loaded from `data/assets.json`) | Pass |
| 18 | Invalid main menu choice | Enter `9` at the main menu | "Invalid choice. Please enter a number between 1 and 8." | Pass |

## How to Run
```
cd src
python3 asset_inventory.py
```

## Notes
- All data is persisted to `data/assets.json` after every add, update, or delete operation.
- Input validation loops until the user supplies an acceptable value for Asset Type, Risk Level, and Security Status.
- Screenshots demonstrating each test case are stored in the `screenshots/` folder (see README for the mapping).
