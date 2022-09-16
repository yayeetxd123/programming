import pyautogui, time
time.sleep(3)
with open("log.txt", "r") as file:
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

