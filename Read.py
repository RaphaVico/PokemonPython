import string

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    global message
    try:
        message = (line.split(":", 2))[2]
    except:
        message = ""
    return message