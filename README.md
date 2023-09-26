# Castle Treasure Mapper

## Overview

This Python script is designed to explore a virtual castle, mapping rooms that contain non-empty chests. It does this by making HTTP requests to a web service providing castle data in JSON format.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Usage

1. Clone this repository to your local machine.

2. Navigate to the directory containing the script.

3. Open the script (`castle_mapper.py`) in a text editor and configure the following constants:

   - `URL_BASE`: The base URL of the castle web service.
   - Optionally, adjust other parameters such as the castle entry point URL if needed.

4. Open a terminal and navigate to the script's directory.

5. Run the script using the following command: python castle_mapper.py

6. The script will start exploring the castle, and it will display the following information:

- Time taken to find all the chests.
- URLs of non-empty chests.
- URLs of rooms with non-empty chests.
- A full map of rooms with non-empty chests.

## Customization

You can customize the script by modifying the `URL_BASE` and other constants to match your specific castle web service URL and structure.
