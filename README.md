### **README.md**
- Logs all keystrokes, including special keys like `Space`, `Enter`, and `Backspace`.
- Saves logged keys to a `log.txt` file in the same directory as the script.
- Option to create a `.exe` file using PyInstaller for easy distribution.

### . Debugging Tips
If the issue persists:
 **Check PyInstaller Logs**:
   PyInstaller logs the build process. Look for error messages in the console.
   
---
####  **Install System-Wide Using `apt`**
For packages available through `apt`, you can use:
```bash
https://github.com/Hackpy3/keylogger
```
```bash
sudo apt install python3-pynput
```
This is the safest method for system-wide installation.

---

####  **Use a Virtual Environment (Recommended)**
Virtual environments isolate your Python dependencies from the system, preventing conflicts. Here's how to use one:

 **Create a Virtual Environment**:
   ```bash
   python3 -m venv myenv
   ```

 **Activate the Virtual Environment**:
   ```bash
   source myenv/bin/activate
   ```

 **Install Required Packages**:
   Inside the activated environment, install the `pynput` library:
   ```bash
   pip install pynput
   ```

 **Run Your Python Scripts**:
   Use the Python interpreter from the virtual environment:
   ```bash
   myenv/bin/python k.py
   ```

 **Deactivate the Environment**:
   When done, deactivate it with:
   ```bash
   deactivate
   ```
Ensure you have `PyInstaller` installed:
```bash
python3 pip install pyinstaller
```

####  **Use `pipx` for Application Isolation**
`pipx` installs Python applications in isolated environments. Install `pipx` first:
```bash
sudo apt install pipx
```

Then, use `pipx` to install and manage the `pynput` library:
```bash
pipx install pynput
```

---

####  **Override System Restriction (Not Recommended)**
If you understand the risks, you can force `pip` to install packages system-wide using:
```bash
pip install --break-system-packages pynput
```
**⚠️ Warning**: This can potentially break system-installed Python applications.

---

###  Run the Keylogger
To start the keylogger, simply execute the script:
```bash
python keylogger.py
```
The keylogger will log all keystrokes to a file named `log.txt`. Press `Esc` to stop the keylogger.


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
