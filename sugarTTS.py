from future import PINMAP
from machine import UART
import time
__version__ = "1.0.5"

class SugarTTS:
    def __init__(self,tx='P2',rx='P12',id=1):
        self.uart = UART(id,9600,tx=PINMAP[tx],rx=PINMAP[rx])
        while True:
            time.sleep(0.5)
            self.uart.write(bytes('K0\n','utf-8'))
            data = self.uart.readline()
            if data:
                try:
                    data = data.decode()
                    if data[0] == 'K' and data[1] == '0':
                        break
                except:
                    pass
        time.sleep(2)

    def mp3_mode(self):
        self.uart.write("K1\n")
        time.sleep(0.3)

    def pause(self):
        self.uart.write("K2\n")
        time.sleep(0.3)

    def stop(self):
        self.uart.write("K3\n")
        time.sleep(0.3)

    def next(self):
        self.uart.write("K4\n")
        time.sleep(0.3)

    def prev(self):
        self.uart.write("K5\n")
        time.sleep(0.3)

    def select_file(self,fileName):
        self.uart.write("K6 %s\n" %(fileName))
        time.sleep(0.3)

    def select_id(self,id):
        self.uart.write("K7 %d\n" %(id))
        time.sleep(0.3)
    
    def tts_mode(self):
        self.uart.write("K8\n")
        time.sleep(0.3)

    def play_text(self,text):
        if text:
            self.uart.write("K9 %s\n" %(text))
    
    def playTextAwait(self,text):
        self.uart.read()
        pauseSymbol = [
            ord("。"),
            ord("，"),
        ]
        grouped_strings = [text[i:i+20] for i in range(0, len(text), 20)]
        for t in grouped_strings:
            delay = 0
            for i in t:
                index = ord(i)
                if index in pauseSymbol:
                    delay+=0.3
                elif index > 127:
                    delay+=0.26
                else:
                    delay+=0.4
            self.uart.write("K10 {}\n".format(t).encode())
            startTime = time.ticks_ms()/1000
            while True:
                if time.ticks_ms()/1000 - startTime > delay+1:
                    break
                state = self.uart.readline()
                if state:
                    if "K10 ok" in state:
                        break