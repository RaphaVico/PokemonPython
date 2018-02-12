import socket
from Settings import  HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(('PASS ' + PASS + '\r\n').encode())
    s.send(('NICK ' + IDENT + '\r\n').encode())
    s.send(('JOIN #' + CHANNEL +'\r\n').encode())
    return  s

def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
    s.send(bytes("PRIVMSG #" + CHANNEL + " :" + message + "\r\n", "UTF-8"))
    # messageTemp = "PRIVMSG #vicuzinho" + CHANNEL + ':' + message
    # s.send((messageTemp + '\r\n').encode("utf-8"))
    print('Sent:' + messageTemp)


