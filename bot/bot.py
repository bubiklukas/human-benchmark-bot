import re
import pyautogui
import time
import keyboard
import win32api, win32con

class Bot(object):

    def getColor():
        pyautogui.displayMousePosition()


    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def ReactionTest(self):
        greenColor = (75, 219, 106)
        mainPixelX = 400
        mainPixelY = 400
        run = False
        while run == False:
            if keyboard.is_pressed('r'):
                run = True

            if keyboard.is_pressed('esc'):
                return

        while run:
            if keyboard.is_pressed('q'):
                    return

            if pyautogui.pixel(400, 400) == greenColor:
                self.click(mainPixelX, mainPixelY)

    def AimTest(self):
        targetColor = (149, 195, 232)

        startX, startY = 600, 200
        endX, endY = startX + 750, startY + 400

        count = 30

        run = False
        while run == False:
            if keyboard.is_pressed('r'):
                run = True

            if keyboard.is_pressed('esc'):
                return
            
        while keyboard.is_pressed('q') == False and run == True:
            ss = pyautogui.screenshot(region=(startX, startY, endX, endY))
            

            br = 0
            while count < 0:
                if keyboard.is_pressed('r'):
                    count = 30
                    ss = pyautogui.screenshot(region=(startX, startY, endX, endY))
                if keyboard.is_pressed('esc'):
                    return
            for x in range(0, ss.width, 20):
                for y in range(0, ss.height, 20):
                    if ss.getpixel((x, y)) == targetColor:
                        self.click(x + startX, y + startY)
                        time.sleep(0.01)
                        count -= 1

                        br = 1
                        break
                if br == 1:
                    break

    def MemoryTest(self):
        whiteColor = (255, 255, 255)

        startX, startY = 750, 220
        endX, endY = startX + 400, startY + 200

        mainss = False
        run = False
        while run == False:
            if keyboard.is_pressed('r'):
                run = True

            if keyboard.is_pressed('esc'):
                return
        while keyboard.is_pressed('q') == False and run == True:
            posList = []

            ss = pyautogui.screenshot(region=(startX, startY, endX, endY))
            for x in range(0, ss.width, 20):
                for y in range(0, ss.height, 20):
                    if ss.getpixel((x, y)) == whiteColor:
                        mainss = True
                        posList.append((x + startX, y + startY))
            if mainss == True:
                time.sleep(3)
                for position in posList:
                    print(position)
                    print(posList)
                    self.click(position[0], position[1])
                mainss = False
                time.sleep(1)

