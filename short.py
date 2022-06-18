import pyautogui, time # time for sleep fn

time.sleep(.5); pyautogui.write(['winleft']); pyautogui.write('anaconda'); pyautogui.write(['enter']);
time.sleep(.5); pyautogui.write('jupyter lab'); pyautogui.write(['enter']);

# installed pyautogui by cmd