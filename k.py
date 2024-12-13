import os

def run_pyinstaller():
    k_py_path = os.path.abspath('k.py')  # Get absolute path for k.py
    if os.path.exists(k_py_path):
        print(f"Building executable for: {k_py_path}")
        os.system(f'pyinstaller --noconfirm --noconsole -F {k_py_path}')
        if os.path.exists('dist/k.exe'):
            print("Executable created successfully!")
        else:
            print("Error: dist/k.exe not found. Please check the PyInstaller command and logs.")
    else:
        print("Error: k.py does not exist in the current directory. Please ensure it is present.")

if __name__ == "__main__":
    run_pyinstaller()
