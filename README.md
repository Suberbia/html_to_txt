# Transform HTML to WhatsApp Chat Format

## Overview

This script allows you to transform HTML files that contain chat messages into a text file formatted like a WhatsApp chat. It's ideal for anyone who wants to convert their chat exports into a more readable format.

## Prerequisites

1. **Python Installed**: Ensure you have Python 3.x installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
2. **BeautifulSoup Library**: This script uses the BeautifulSoup library to parse HTML. You will need to install it if it's not already installed.

## Installation

### Step 1: Install Python

Download and install Python from the [official website](https://www.python.org/downloads/). Follow the instructions for your operating system.

### Step 2: Install Required Libraries

Open your command prompt (Windows) or terminal (macOS/Linux) and run the following command to install the BeautifulSoup library:

```bash
pip install beautifulsoup4
```

## Usage

### Step 1: Download the Script

Save the provided script into a file named `transform_html_to_whatsapp.py`.

### Step 2: Prepare Your HTML File

Ensure your chat messages are saved in an HTML file (e.g., `messages.html`).

### Step 3: Run the Script

1. **Open Command Prompt or Terminal**

   - On Windows: Press `Win + R`, type `cmd`, and press Enter.
   - On macOS/Linux: Open your terminal from the Applications folder or via a shortcut.

2. **Navigate to the Directory Containing the Script and HTML File**

   Use the `cd` command to change the directory to where you saved `transform_html_to_whatsapp.py` and `messages.html`.

   ```bash
   cd path/to/your/directory
   ```

3. **Run the Script**

   Execute the script by running:

   ```bash
   python transform_html_to_whatsapp.py
   ```

4. **Wait for the Script to Complete**

   The script will read your HTML file, transform the content, and save it to `_chat.txt`. You will see a message indicating the transformation is complete.

### Example Commands

Here is a detailed example of the commands you might run:

```bash
pip install beautifulsoup4
cd C:\Users\YourUsername\Documents\YourDirectory  # Navigate to your directory
python transform_html_to_whatsapp.py             # Run the script
```

### Output

After running the script, you'll find a file named `_chat.txt` in the same directory. This file contains the transformed chat messages in WhatsApp format.

## Troubleshooting

- **Ensure BeautifulSoup is Installed**: If you receive an error about BeautifulSoup not being found, make sure you've installed the library using the `pip install beautifulsoup4` command.
- **Check File Paths**: Make sure your HTML file and the script are in the correct directory. Use the `ls` (macOS/Linux) or `dir` (Windows) command to list files in the current directory to verify.
- **Python Version**: Ensure you're using Python 3.x by running `python --version`.

## Additional Notes

- Customize the HTML parsing in the script if your HTML file structure differs.
- Test with a small sample HTML file first to ensure it works as expected.
