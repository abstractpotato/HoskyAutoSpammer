import pyautogui, time

print("starting raffle in 5s")
time.sleep(5)

pyautogui.write("/raffle", 0.1)
pyautogui.press("tab")
pyautogui.write("10m", 0.1)
pyautogui.press("tab")
if random.random() > .5:
    pyautogui.write("1000000 STRCH", 0.1)
else:
    pyautogui.write("1000000 HOSKY", 0.1)
pyautogui.press("enter")

time.sleep(60*3)

print("goodbye")