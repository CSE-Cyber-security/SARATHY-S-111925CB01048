"""
Cybersecurity Asset Inventory System
Weekly Mini Project - 01

A menu-driven CLI application to add, search, update, delete, and
display an organization's IT assets, classified by asset type,
risk level, and security status.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def load_assets():
    """Load assets from the JSON data file. Returns an empty list if the
    file does not exist or is empty/corrupt."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, OSError):
        return []


def save_assets(assets):
    """Persist the asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------------------
# Input validation helpers
# ---------------------------------------------------------------------------

def get_nonempty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Please try again.")


def get_choice_input(prompt, choices):
    choice_str = "/".join(choices)
    while True:
        value = input(f"{prompt} ({choice_str}): ").strip()
        for c in choices:
            if value.lower() == c.lower():
                return c
        print(f"  Invalid entry. Please choose one of: {choice_str}")


def get_unique_asset_id(assets, prompt="Asset ID: "):
    while True:
        asset_id = get_nonempty_input(prompt)
        if any(a["asset_id"].lower() == asset_id.lower() for a in assets):
            print("  An asset with this ID already exists. Please enter a different ID.")
            continue
        return asset_id


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset_id = get_unique_asset_id(assets)
    asset = {
        "asset_id": asset_id,
        "asset_name": get_nonempty_input("Asset Name: "),
        "asset_type": get_choice_input("Asset Type", ASSET_TYPES),
        "ip_address": get_nonempty_input("IP Address: "),
        "operating_system": get_nonempty_input("Operating System: "),
        "department": get_nonempty_input("Owner/Department: "),
        "risk_level": get_choice_input("Risk Level", RISK_LEVELS),
        "security_status": get_choice_input("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"\nAsset '{asset_id}' added successfully.")


def add_multiple_assets(assets):
    try:
        count = int(get_nonempty_input("Enter number of assets: "))
    except ValueError:
        print("  Invalid number.")
        return
    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        add_asset(assets)


def find_asset(assets, asset_id):
    for asset in assets:
        if asset["asset_id"].lower() == asset_id.lower():
            return asset
    return None


def search_asset(assets):
    print("\n--- Search Asset ---")
    asset_id = get_nonempty_input("Enter Asset ID to search: ")
    asset = find_asset(assets, asset_id)
    if asset:
        print("\nAsset found:")
        print_asset(asset)
    else:
        print(f"\nNo asset found with ID '{asset_id}'.")


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = get_nonempty_input("Enter Asset ID to update: ")
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"\nNo asset found with ID '{asset_id}'.")
        return

    print("Leave a field blank to keep its current value.")
    print(f"Current Asset Name [{asset['asset_name']}]:")
    name = input("New Asset Name: ").strip()
    if name:
        asset["asset_name"] = name

    print(f"Current Asset Type [{asset['asset_type']}]:")
    atype = input(f"New Asset Type ({'/'.join(ASSET_TYPES)}) or blank: ").strip()
    if atype:
        for c in ASSET_TYPES:
            if atype.lower() == c.lower():
                asset["asset_type"] = c
                break

    print(f"Current IP Address [{asset['ip_address']}]:")
    ip = input("New IP Address: ").strip()
    if ip:
        asset["ip_address"] = ip

    print(f"Current Operating System [{asset['operating_system']}]:")
    os_ = input("New Operating System: ").strip()
    if os_:
        asset["operating_system"] = os_

    print(f"Current Department [{asset['department']}]:")
    dept = input("New Owner/Department: ").strip()
    if dept:
        asset["department"] = dept

    print(f"Current Risk Level [{asset['risk_level']}]:")
    risk = input(f"New Risk Level ({'/'.join(RISK_LEVELS)}) or blank: ").strip()
    if risk:
        for c in RISK_LEVELS:
            if risk.lower() == c.lower():
                asset["risk_level"] = c
                break

    print(f"Current Security Status [{asset['security_status']}]:")
    status = input(f"New Security Status ({'/'.join(SECURITY_STATUSES)}) or blank: ").strip()
    if status:
        for c in SECURITY_STATUSES:
            if status.lower() == c.lower():
                asset["security_status"] = c
                break

    save_assets(assets)
    print(f"\nAsset '{asset_id}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = get_nonempty_input("Enter Asset ID to delete: ")
    asset = find_asset(assets, asset_id)
    if not asset:
        print(f"\nNo asset found with ID '{asset_id}'.")
        return
    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print(f"\nAsset '{asset_id}' deleted successfully.")
    else:
        print("\nDelete cancelled.")


# ---------------------------------------------------------------------------
# Display / reporting
# ---------------------------------------------------------------------------

def print_asset(asset):
    print(f"Asset ID       : {asset['asset_id']}")
    print(f"Asset Name     : {asset['asset_name']}")
    print(f"Asset Type     : {asset['asset_type']}")
    print(f"IP Address     : {asset['ip_address']}")
    print(f"OS             : {asset['operating_system']}")
    print(f"Department     : {asset['department']}")
    print(f"Risk Level     : {asset['risk_level']}")
    print(f"Status         : {asset['security_status']}")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No assets found.")
        print("=========================================")
        return

    for i, asset in enumerate(assets):
        print_asset(asset)
        if i < len(assets) - 1:
            print("-----------------------------------------")

    print("=========================================")
    print_summary(assets)
    print("=========================================")


def print_summary(assets):
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    low = sum(1 for a in assets if a["risk_level"] == "Low")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")
    warning = sum(1 for a in assets if a["security_status"] == "Warning")
    secure = sum(1 for a in assets if a["security_status"] == "Secure")

    print(f"Total Assets : {total}")
    print(f"Critical Assets : {critical}")
    print(f"High Risk Assets : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Low Risk Assets : {low}")
    print(f"Vulnerable Assets : {vulnerable}")
    print(f"Warning Assets : {warning}")
    print(f"Secure Assets : {secure}")


# ---------------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------------

def print_menu():
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
    print("=========================================")
    print("1. Add Asset")
    print("2. Add Multiple Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Display All Assets")
    print("7. Security Summary")
    print("8. Exit")


def main():
    assets = load_assets()

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            display_assets(assets)
        elif choice == "7":
            print("\n=========================================")
            print(" SECURITY SUMMARY")
            print("=========================================")
            print_summary(assets)
            print("=========================================")
        elif choice == "8":
            print("\nExiting Cybersecurity Asset Inventory System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
