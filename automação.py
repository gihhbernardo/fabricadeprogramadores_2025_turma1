import mouseinfo, pyautogui, time


mouseinfo.mouseInfo()

pyautogui.moveTo(987,1061,duration=2)
pyautogui.moveTo(737,138,duration=2)
pyautogui.click()
time.sleep(1)
pyautogui.write("facebook")
time.sleep(1)
pyautogui.click()