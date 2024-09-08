# this is possibly the worst script i've ever made

import win32api, win32con, time, pyautogui, pyperclip

SCREEN_X = 2307 # this is where the text from other ppl is
SCREEN_Y = 938

AI_SCREEN_X = 3500 # chat gpt where you can type
AI_SCREEN_Y = 980

AI_FUCK_X = 3262 # where the text appears for chat gpt
AI_FUCK_Y = 826

TYPE_SCREEN_X = 2480 # where ur discord typing shit is
TYPE_SCREEN_Y = 990

def click(x, y):
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
		time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def run_through():
    for x in range(1, 4):
        click(SCREEN_X, SCREEN_Y)
        time.sleep(0.2)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    prompt = pyperclip.paste()

    click(AI_SCREEN_X, AI_SCREEN_Y)
    time.sleep(0.5)

    pyperclip.copy(prompt)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.hotkey('enter')

    time.sleep(6.0) # this the big wait? okay matt? because im literally fucking blind and retarded i spent 3 minutes looking for this line

    for x in range(1, 4):
        click(AI_FUCK_X, AI_FUCK_Y)
        time.sleep(0.2)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    prompt = pyperclip.paste()

    click(TYPE_SCREEN_X, TYPE_SCREEN_Y)
    time.sleep(0.5)

    pyperclip.copy(prompt)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.hotkey('enter')

# uhh just close visual studio code to stop this shit

while True:
    run_through()
    time.sleep(60)
