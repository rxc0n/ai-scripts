import requests

# Function to fetch avatar information
def get_avatar_info(username):
    # Roblox API endpoint for user information
    api_url = f'https://api.roblox.com/users/get-by-username?username={username}'

    # Make a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_info = response.json()

        # Check if the user exists
        if 'Id' in user_info:
            user_id = user_info['Id']

            # Roblox API endpoint for avatar information
            avatar_url = f'https://avatar.roblox.com/v1/users/{user_id}/avatar'
            
            # Make a GET request to the avatar API
            avatar_response = requests.get(avatar_url)
            
            # Check if the avatar request was successful
            if avatar_response.status_code == 200:
                # Parse the JSON response
                avatar_info = avatar_response.json()

                # Print avatar information
                print(f"Username: {username}")
                print(f"Avatar URL: {avatar_info['Url']}")
                print("\nAccessories:")
                for accessory in avatar_info['assets']:
                    print(f"{accessory['name']} - {accessory['assetId']}")

            else:
                print(f"Failed to fetch avatar information. Status Code: {avatar_response.status_code}")

        else:
            print(f"User '{username}' not found.")

    else:
        print(f"Failed to fetch user information. Status Code: {response.status_code}")

# Get Roblox username from the user
roblox_username = input("Enter a Roblox username: ")

# Fetch and display avatar information
get_avatar_info(roblox_username)
