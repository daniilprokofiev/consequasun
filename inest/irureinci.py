import os
import platform

def is_rebooting():
    if platform.system() == 'Darwin':  # macOS
        return os.popen('sysctl -n hw.boottime').read().strip() != str(int(time.time()))
    elif platform.system() == 'Linux':  # Linux
        return os.popen('cat /proc/stat').read().strip() != str(int(time.time()))
    else:  # Windows
        return os.popen('wmic os get lastbootuptime').read().strip() != str(int(time.time()))
