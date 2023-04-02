"""It is used to remove generated password from clipboard in 45 seconds"""
import time

import pyclip

if __name__ == "__main__":
    time.sleep(45)
    pyclip.clear()
