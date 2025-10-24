import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # ekran tozalash
    print("🔴 Qizil — To'xta")
    time.sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟡 Sariq — Tayyorlaning")
    time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("🟢 Yashil — Yuring")
    time.sleep(3)