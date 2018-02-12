import string
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Read import getUser, getMessage
from Settings import VK_CODE
import win32api
import time
import win32con

s = openSocket()
joinRoom(s)
readbuffer = ""
while True:
    readbuffer = s.recv(1024)
    readbuffer = readbuffer.decode()
    temp = readbuffer.split("\n")
    readbuffer = readbuffer.encode()
    readbuffer = temp.pop()

    for line in temp:
        print(line)
        user = getUser(line)
        message = getMessage(line)
        print(user + " > " + message)
        if "PING" in line:
            msgg = "PONG tmi.twitch.tv\r\n".encode()
            s.send(msgg)
            print(msgg)
            break
        if '#A' in message:
            win32api.keybd_event(VK_CODE['x'], 0, 0, 0)
            time.sleep(0.05)
            win32api.keybd_event(VK_CODE['x'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão A')
            break
        if '#B' in message:
            win32api.keybd_event(VK_CODE['z'], 0, 0, 0)
            time.sleep(0.05)
            win32api.keybd_event(VK_CODE['z'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão B')
            break
        if '#Up' in message:
            win32api.keybd_event(VK_CODE['up_arrow'], 0, 0, 0)
            time.sleep(0.2)
            win32api.keybd_event(VK_CODE['up_arrow'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão Up')
            break
        if '#Down' in message:
            win32api.keybd_event(VK_CODE['down_arrow'], 0, 0, 0)
            time.sleep(0.2)
            win32api.keybd_event(VK_CODE['down_arrow'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão Down')
            break
        if '#Right' in message:
            win32api.keybd_event(VK_CODE['right_arrow'], 0, 0, 0)
            time.sleep(0.2)
            win32api.keybd_event(VK_CODE['right_arrow'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão Right')
            break
        if '#Left' in message:
            win32api.keybd_event(VK_CODE['left_arrow'], 0, 0, 0)
            time.sleep(0.2)
            win32api.keybd_event(VK_CODE['left_arrow'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão Left')
            break
        # if 'L' in message:
        #     win32aapi.keybd_event(VK_CODE['a'], 0, 0, 0)
        #     time.sleep(0.2)
        #     win32api.keybd_event(VK_CODE['a'], 0, win32con.KEYEVENTF_KEYUP, 0)
        #     print('Botão L')
        #     break
        # if 'R' in message:
        #     win32api.keybd_event(VK_CODE['s'], 0, 0, 0)
        #     time.sleep(0.2)
        #     win32api.keybd_event(VK_CODE['s'], 0, win32con.KEYEVENTF_KEYUP, 0)
        #     print('Botão R')
        #     break
        if '#Start' in message:
            win32api.keybd_event(VK_CODE['i'], 0, 0, 0)
            time.sleep(0.2)
            win32api.keybd_event(VK_CODE['i'], 0, win32con.KEYEVENTF_KEYUP, 0)
            print('Botão Start')
            break
        # if 'Select' in message:
        #     win32api.keybd_event(VK_CODE['u'], 0, 0, 0)
        #     time.sleep(0.2)
        #     win32api.keybd_event(VK_CODE['u'], 0, win32con.KEYEVENTF_KEYUP, 0)
        #     print('Botão Select')
        #
        #     break

        if '!ping' in message:
            sendMessage(s, 'PONG')
            print('PING-PONG')
            break

