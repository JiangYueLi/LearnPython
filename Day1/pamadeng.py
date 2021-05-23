"""
屏幕上显示跑马灯文字。
"""

import os
import time

def main():
    content = '你还爱我么'
    while True:
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()