
# DiscordSecureToken

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Python script to automate the refresh of a Discord token.

## Description

This Python script allows you to automatically refresh your Discord token at a specified interval. It utilizes the Discord API to refresh the token and provides the new token as output when the refresh is successful.

## Features

- Set a custom refresh interval in minutes (1-60).
- Automatically refreshes the token based on the configured interval.
- Displays the new token when the refresh is successful.

## Prerequisites

- Python 3.6 or above
- `requests` library (install with `pip install requests`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/discord-token-refresh.git
   cd discord-token-refresh
   ```

2. Install the required dependencies:

   ```bash
   pip install requests
   ```

3. Replace `'YOUR_OLD_TOKEN'` with your actual old token in the `refresh_token_periodically` function.

4. Run the script:

   ```bash
   python DiscordSecureToken.py
   ```

5. Follow the configuration menu prompts to set the refresh interval and start the token refresh process.

6. The script will automatically refresh the token at the specified interval and display the new token when the refresh is successful.

## Upcoming Features
- Automaticly get Token and Refesh it

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
