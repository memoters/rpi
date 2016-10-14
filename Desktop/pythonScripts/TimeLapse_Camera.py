import pifacecad
from pifacecad import *
import picamera
from picamera import *
from time import sleep

captureCount = 0;
isQuit = 0;

class Watcher(object):
    def __init__(self):
        super().__init__()
        self.listener = pifacecad.SwitchEventListener()
        for i in range(8):
            self.listener.register(
                i, pifacecad.IODIR_BOTH, self.button_pressed)


    def initializeClass(self):
        self.listener.activate()

    def button_pressed(self, event):
        if   (event.pin_num == 0):
            isQuit = 1
            timelapsCam.switch_0()
        elif (event.pin_num == 1):
            timelapsCam.switch_1()
        elif (event.pin_num == 2):
            timelapsCam.switch_2()
        elif (event.pin_num == 3):
            timelapsCam.switch_3()
        elif (event.pin_num == 4):
            timelapsCam.switch_4()
            
            
class TimelapseCamera(object):

    def __init__(self):
        super().__init__()
        
    def switch_0(event):
        cad.lcd.backlight_off()
##        cad.lcd.clear()
##        exit()
        
    def switch_1(event):
        cad.lcd.backlight_on()
           
    def switch_2(event):
        global captureCount        
        filename = "/home/pi/Desktop/photos/Photo_" + str(captureCount) + ".jpg"
        cam.capture(str(filename))
        captureCount = captureCount + 1    
        cad.lcd.write("Filename: " + str(filename))
        sleep(2)
        cad.lcd.clear()        

    def switch_3(event):
        cad.lcd.write("Timelapse!")
        sleep(2)
        for i in range(3):        
            cad.lcd.write("Starting in :" + str(i))
            sleep(1)
            cad.lcd.clear()
            
        filename = "/home/pi/Desktop/photos/Timelapse/TM_"
        ##+ str(captureCount) + ".jpg"
        sleep(2)
        for fn in cam.capture_continuous(filename + '{counter:02d}.jpg'):
            if(isQuit == 1):
                break
            cad.lcd.write("Filename: " + str(fn))
            sleep(10)
            cad.lcd.clear()
        cad.lcd.clear()

##    def switch_4(event):

class Splash(object):    
    def __init__(self):
        super().__init__()

    W_block = pifacecad.LCDBitmap(
        [0b10001,
         0b10001,
         0b10001,
         0b10101,
         0b10101,
         0b11111,
         0b00000,
         0b11111,])
    E_block = pifacecad.LCDBitmap(
        [0b11111,
         0b10000,
         0b11000,
         0b11000,
         0b10000,
         0b11111,
         0b00000,
         0b11111,])
    L_block = pifacecad.LCDBitmap(
        [0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b11111,
         0b00000,
         0b11111,])
    C_block = pifacecad.LCDBitmap(
        [0b11111,
         0b10001,
         0b10000,
         0b10000,
         0b10001,
         0b11111,
         0b00000,
         0b11111,])
    O_block = pifacecad.LCDBitmap(
        [0b11111,
         0b10001,
         0b10101,
         0b10101,
         0b10001,
         0b11111,
         0b00000,
         0b11111,])
    M_block = pifacecad.LCDBitmap(
        [0b10001,
         0b11011,
         0b10101,
         0b10101,
         0b10001,
         0b10001,
         0b00000,
         0b11111,])

    def constructHeaderBLock(self):
        cad.lcd.set_cursor(0,0)
        cad.lcd.write_custom_bitmap(0,self.W_block)
        cad.lcd.write_custom_bitmap(1,self.E_block)
        cad.lcd.write_custom_bitmap(2,self.L_block)
        cad.lcd.write_custom_bitmap(3,self.C_block)
        cad.lcd.write_custom_bitmap(4,self.O_block)
        cad.lcd.write_custom_bitmap(5,self.M_block)
        cad.lcd.write_custom_bitmap(6,self.E_block)

    
    def ShowSplash(self):
        self.constructHeaderBLock()
        
        
    
if __name__ == "__main__":     
    cad = pifacecad.PiFaceCAD()
    cad.lcd.clear()
    cam = picamera.PiCamera()
    timelapsCam = TimelapseCamera()

    splash = Splash()
    splash.ShowSplash()
    
    sleep(5)

    
    
    try:
        myWatcher = Watcher()
        myWatcher.initializeClass()
    except:
        quit()

##    while True:
##        for i in range(8):            
##            if cad.switches[i].value == 1:
##                if i == 0:
##                    switch_0(i)
##                elif i == 1:
##                    switch_1(i)
##                elif i == 2:
##                    switch_2(i)
##                elif i == 3:
##                    switch_3()
##        sleep(0.2)
##    
