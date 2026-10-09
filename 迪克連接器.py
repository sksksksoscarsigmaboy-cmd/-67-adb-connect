#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

def connect_adb():
    print("\n====================================")
    print("   阿公67 ADB 一鍵連接愛潑斯坦島😭🙏  ")
    print("====================================")

    try:
        ip = input("請輸入迪克裝置 IP (例如 192.168.1.100): ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n阿公67摔倒了😭🙏")
        sys.exit()

    if not ip:
        print("錯誤：IP🫢 ")
        return

    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        print(f"錯誤遇到扶他🙏：'{ip}' 不是正確的迪克")
        return

    try:
        port_input = input("請輸入阿公67裏面的迪克連接埠🥀 [直接按 Enter 預設為 5555🫢]: ").str>
    except (KeyboardInterrupt, EOFError):
        print("\n迪克被剪斷了🥀🙏")
        sys.exit()

    port = port_input if port_input else "5555"

    print(f"\n正在嘗試連接到迪克裝置 {ip}:{port} ...")

    command = f"adb connect {ip}:{port}"
    result = os.system(command)

    print("====================================")
    if result == 0:
            print("阿公67裏面的迪克連接已連接")
        print("請在愛潑斯坦島檢查阿公67有沒有連接成功🧓67")
    else:
        print("阿公67摔倒了 請確認 Termux 內是否有安裝 adb 設備。")
    print("====================================\n")

if __name__ == "__main__":
    connect_adb()
