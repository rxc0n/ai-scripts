import requests
import time

# Function to check if an asset is on sale
def check_onsale(asset_ids):
    while True:
        for asset_id in asset_ids:
            # Roblox API endpoint for asset information
            api_url = f'https://api.roblox.com/marketplace/productinfo?assetId={asset_id}'

            # Make a GET request to the API
            response = requests.get(api_url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                asset_info = response.json()

                # Check if the asset is on sale
                if asset_info['IsForSale']:
                    print(f"Alert: Asset '{asset_info['Name']}' (ID: {asset_id}) is on sale!")
                else:
                    print(f"Asset '{asset_info['Name']}' (ID: {asset_id}) is not on sale.")

            else:
                print(f"Failed to fetch asset information for ID {asset_id}. Status Code: {response.status_code}")

        # Wait for 3 seconds before checking again
        time.sleep(3)

# Get up to 5 asset IDs from the user
asset_ids_input = input("Enter up to 5 asset IDs separated by commas: ")
user_asset_ids = [int(asset_id.strip()) for asset_id in asset_ids_input.split(',')]

# Check if the user provided at least one asset ID
if user_asset_ids:
    # Start checking for on-sale items
    check_onsale(user_asset_ids)
else:
    print("No asset IDs provided. Exiting.")
