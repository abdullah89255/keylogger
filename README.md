### **README.md**
- Logs all keystrokes, including special keys like `Space`, `Enter`, and `Backspace`.
- Saves logged keys to a `log.txt` file in the same directory as the script.
- Option to create a `.exe` file using PyInstaller for easy distribution.


---
####  **Install **

```bash
git clone https://github.com/Hackpy3/keylogger
cd keylogger
```
---

####  **Use a Virtual Environment (Recommended)**
Virtual environments isolate your Python dependencies from the system, preventing conflicts. Here's how to use one:



 **Install Required Packages**:
   Inside the activated environment, install the `pynput` library:
   ```bash
   pip install pynput --break-system-packages
   ```
```bash
 pip install pyinstaller --break-system-packages
```
```bash
sudo apt install pipx
```
 **Create a Virtual Environment**:
   ```bash
   python3 -m venv myenv
   ```

   ```bash
   myenv/bin/python k.py
   ```
###  Run the Keylogger
To start the keylogger, simply execute the script:
```bash
python keylogger.py
```

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
