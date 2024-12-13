### **README.md**
Here’s the `README.md` file that explains the project and provides an example:

```markdown
# Keylogger with Executable Creation 🖥️🔑

This Python script is a basic keylogger for educational purposes. It logs all keystrokes into a `log.txt` file and includes functionality to create a standalone executable using PyInstaller.

## Features ✨
- Logs all keystrokes, including special keys like `Space`, `Enter`, and `Backspace`.
- Saves logged keys to a `log.txt` file in the same directory as the script.
- Option to create a `.exe` file using PyInstaller for easy distribution.

## Usage 🚀

### 1. Run the Keylogger
To start the keylogger, simply execute the script:
```bash
python keylogger.py
```
The keylogger will log all keystrokes to a file named `log.txt`. Press `Esc` to stop the keylogger.

### 2. Create an Executable
To create a standalone executable:
```bash
python keylogger.py --create-exe
```
Ensure you have `PyInstaller` installed:
```bash
pip install pyinstaller
```

### Example 📝
#### Running the Keylogger:
```bash
python keylogger.py
```
- Typed: `Hello World!`
- Logged Output in `log.txt`:
  ```
  Hello World!
  ```

#### Creating the Executable:
```bash
python keylogger.py --create-exe
```
Output: A standalone `.exe` file will be created in the `dist` directory.

## Requirements 📦
- Python 3.6 or higher
- Libraries:
  - `pynput`
  - `pyinstaller`

## Disclaimer ⚠️
This script is for **educational purposes only**. Do not use it for malicious activities. Always ensure you have permission to log keystrokes on the device you are using.

---

**Happy Coding! 😄**
```

---

Let me know if you need further customization or guidance!
