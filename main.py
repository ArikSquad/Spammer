# Imports
import pyautogui
import time

#
# Made by Ari k.
# Youtube: Youtube.com/arikchannel
# Github: github.com/ariksquad
#
# Variables
name = str("AriSpammer")
print("AriModules")
print(f"Currently using the {name}")
spam = str(input("Spamming > "))
times = int(input("Times > "))

# Check if string is return.
if spam is not None:
    print(f"Okay, so we are spamming ({spam})! Waiting 5 seconds")
# If not then use your last copy.
else:
    print(f"Okay, so we are spamming your paste! Waiting 5 seconds")

# Start sleeping
time.sleep(5)
print("Starting")

# The variables to show how many times it's been ran.
s = 0
a = 1

# loop
for i in range(times):
    # Make the times.
    s = s + a

    # If string is returned then spam the string
    if spam is not None:
        pyautogui.typewrite(spam)

    # If the string is not returned then paste
    else:
        pyautogui.hotkey('ctrl', 'v', interval=0.15)

    # Send the message. Usually the 'enter' key.
    pyautogui.press("enter")

    # Prints how many times it's been ran.
    print(f"Did this {s} times")

# Prints Successful after all.
print("Successful!")
# Exits the program safely.
exit()
