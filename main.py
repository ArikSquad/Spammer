import pyautogui
import time


spam = str(input("The text you want to spam? > "))
times = int(input("How many times? > "))

if spam is not None:
    print(f"Okay, so we are spamming ({spam})! Waiting 5 seconds")
else:
    print(f"Okay, so we are spamming your clipboard! Waiting 5 seconds")

time.sleep(5)
print("Starting the spammer")

s = 0

for i in range(times):
    s = s + 1

    if spam is not None:
        pyautogui.typewrite(spam)
    else:
        pyautogui.hotkey('ctrl', 'v', interval=0.15)
    pyautogui.press("enter")

    print(f"Sent keystrokes {s} times")

print(f"Spammer end. {s} times in total.")
exit()
