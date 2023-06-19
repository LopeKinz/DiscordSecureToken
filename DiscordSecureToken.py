import requests
import json
import time

def refresh_token(token):
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        'token': token,
    }

    response = requests.post('https://discord.com/api/v9/auth/token', headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_data = response.json()
        new_token = response_data['token']
        return new_token
    else:
        print('Token refresh failed with status code:', response.status_code)
        return None

def configuration_menu():
    print("Token Refresh Configuration")
    print("---------------------------")
    print("1. Set Refresh Interval")
    print("2. Start Token Refresh")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        set_refresh_interval()
    elif choice == '2':
        start_token_refresh()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Please try again.")
        configuration_menu()

def set_refresh_interval():
    interval = input("Enter the refresh interval in minutes (1-60): ")
    
    try:
        interval = int(interval)
        if interval < 1 or interval > 60:
            raise ValueError
    except ValueError:
        print("Invalid input. Interval must be an integer between 1 and 60.")
        set_refresh_interval()
    
    while True:
        refresh_token_periodically(interval)
        time.sleep(interval * 60)

def refresh_token_periodically(interval):
    old_token = input("Enter your old token: ")
    new_token = refresh_token(old_token)
    
    if new_token:
        print('New token:', new_token)
    
        print("Waiting for the next refresh in", interval, "minutes...")
        print("----------------------------------------------")
    else:
        print("Token refresh failed. Retrying in", interval, "minutes...")
        print("------------------------------------------------")

def start_token_refresh():
    interval = input("Enter the refresh interval in minutes (1-60): ")
    
    try:
        interval = int(interval)
        if interval < 1 or interval > 60:
            raise ValueError
    except ValueError:
        print("Invalid input. Interval must be an integer between 1 and 60.")
        start_token_refresh()
    
    refresh_token_periodically(interval)
    time.sleep(interval * 60)

# Entry point
configuration_menu()
