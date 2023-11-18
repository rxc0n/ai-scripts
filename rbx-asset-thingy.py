import requests

# Function to fetch asset information
def get_asset_info(asset_id):
    # Roblox API endpoint for asset information
    api_url = f'https://api.roblox.com/marketplace/productinfo?assetId={asset_id}'

    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        asset_info = response.json()

        # Print asset information
        print(f"Asset Name: {asset_info['Name']}")
        print(f"Asset Description: {asset_info['Description']}")
        print(f"Asset ID: {asset_info['AssetId']}")
        print(f"Creator: {asset_info['Creator']['Name']}")
        print(f"Sales: {asset_info['Sales']}")
        
        # Fetch and display the asset image
        image_url = f'https://www.roblox.com/asset-thumbnail/image?assetId={asset_id}&width=420&height=420&format=png'
        image_response = requests.get(image_url)
        with open(f'asset_{asset_id}_image.png', 'wb') as image_file:
            image_file.write(image_response.content)
        print(f"Asset Image saved as asset_{asset_id}_image.png")

    else:
        print(f"Failed to fetch asset information. Status Code: {response.status_code}")

# Example: Fetch information for a specific asset (replace 'ASSET_ID' with the desired asset ID)
asset_id_to_fetch = 'ASSET_ID'
get_asset_info(asset_id_to_fetch)
