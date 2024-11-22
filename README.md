# Task 4: Simple Keylogger

## Overview
This project creates a basic keylogger that logs all keyboard inputs and saves them to a file. **Use it responsibly and only with permission.**

## Features
- Logs all keypresses, including special keys (e.g., Enter, Space).
- Saves the log to a text file.
- Easy-to-understand implementation.

## How to Use
1. Ensure you have the necessary permissions (macOS users: add Python to Accessibility settings).
2. Run the script.
3. Keypresses will be saved in the specified log file (default: `keylog.txt`).

## Requirements
- Python 3.x
- pynput library (`pip install pynput`)

## Ethical Disclaimer
This tool is intended for educational purposes only. Unauthorized use is strictly prohibited.

## File Structure
- **`Task4SimpleKeylogger.py`**: Python script containing the keylogger implementation.
- **`keylog.txt`**: The log file where keystrokes are recorded.

## Prerequisites
- Python 3.x installed on your system.
- `pynput` library installed. To install it, run:
  ```bash
  pip install pynput
## Usage Instructions
Clone or download this repository to your local machine.
Install the required library:
pip install pynput
Open the terminal and navigate to the project directory:
bash

cd /path/to/project
Run the keylogger script:

python Task4SimpleKeylogger.py
Type in any application (e.g., TextEdit, Terminal, or Word) while the script is running.
Stop the script by pressing Ctrl+C in the terminal.
Open the keylog.txt file to view the recorded keystrokes.
## Debugging
If the keylogger is not capturing keystrokes:

## Enable Debugging:

Add a print statement inside the log_keystroke function:

print(f"Key pressed: {key}")
This will print every captured key to the terminal during execution.

## Verify Accessibility Permissions:

On macOS, ensure your Python interpreter or IDE has the necessary permissions:
Go to System Preferences > Privacy & Security > Accessibility.
Add the Python executable or your IDE (e.g., PyCharm) to the list and enable it.
If required, enable Input Monitoring or Full Disk Access in the same settings.

## Test in a Simple Application:

Try typing in basic applications like TextEdit or Terminal, as some applications (e.g., Word) may restrict key monitoring.

## Run as Administrator:

If permissions are still an issue, run the script with elevated privileges:
sudo python Task4SimpleKeylogger.py
Permissions
## macOS Users:
Grant Accessibility Permissions to your Python interpreter or IDE:
Go to System Preferences > Privacy & Security > Accessibility.
Add your Python interpreter or PyCharm to the list.
If required, enable Input Monitoring or Full Disk Access.
## Ethical Disclaimer
This project is intended for educational purposes only. Unauthorized use of keyloggers is illegal and can lead to severe legal consequences. Use this tool responsibly and only with explicit permission.
