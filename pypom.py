import subprocess
import time
import ctypes
import sys
import os

def pomodoro(val, duration):
    print('\n > '+val+'\n')
    subprocess.run(["timer.exe", str(duration * 60)])
    ctypes.windll.user32.MessageBoxW(None, "'{}' session done".format(val), "Pomodoro Timer", 0x40 | 0x1)
    print("'{}' session done".format(val))

def main():
    work_duration = int(input("Enter Work session : "))
    break_duration = int(input("Enter Break session : "))
    try:
        i = 1
        while True:
            print("Session Count: {}".format(i))
            pomodoro("WORK", work_duration)
            os.system("cls" if os.name == "nt" else "clear")
            pomodoro("BREAK", break_duration)
            os.system("cls" if os.name == "nt" else "clear")
            i = i+1

            
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)

if __name__ == '__main__':
    main()
