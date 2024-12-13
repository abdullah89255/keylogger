import os

def get_absolute_path(file_name):
    """Return the absolute path of the given file."""
    return os.path.abspath(file_name)

def main():
    k_py_path = get_absolute_path('k.py')  # Dynamically determine absolute path for k.py
    if os.path.exists(k_py_path):
        print(f"Absolute path to k.py: {k_py_path}")
        os.system(f'pyinstaller --noconfirm --noconsole -m Manifest/manifest.manifest -F {k_py_path}')
    else:
        print("Error: k.py does not exist in the current directory. Please ensure it is present.")

if __name__ == "__main__":
    main()
