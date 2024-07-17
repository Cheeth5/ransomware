import sys
import platform
import subprocess

def main():
    operating_system = platform.system()

    if operating_system == "Linux":
        # Linux shutdown or lock command
        shutdown_command = "sudo /sbin/shutdown -h now"
        lock_command = "gnome-screensaver-command -l"
    elif operating_system == "Darwin":
        # macOS shutdown or lock command
        shutdown_command = "sudo /sbin/shutdown -h now"
        lock_command = "open -a /System/Library/CoreServices/ScreenSaverEngine.app -W"
    elif operating_system == "Windows":
        # Windows shutdown or lock command
        shutdown_command = "shutdown /s /t 1"
        lock_command = "rundll32.exe user32.dll,LockWorkStation"
    else:
        print(f"Unsupported operating system: {operating_system}")
        return

    try:
        # Execute shutdown or lock command
        subprocess.run(shutdown_command.split(), check=True)
        print(f"{operating_system} shutting down...")
    except subprocess.CalledProcessError as e:
        print(f"Error executing shutdown command: {e}")

    try:
        # Execute lock command (if applicable)
        subprocess.run(lock_command.split(), check=True)
        print(f"{operating_system} locked.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing lock command: {e}")

if __name__ == "__main__":
    main()
