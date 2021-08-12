def infoLogger(message):
    #print(f'INFO: {str(message)}')
    #msg = str(message).split()[0]
    #if (msg == "key.ctrl_l"):
    #    x=0
    #else:
    #    print(msg) #this line is for key recognition
    log = open("logs.txt", "a")
    log.write(f'INFO: {str(message)}\n')
    log.close()

def warningLogger(message):
    #print(f'WARNING: {str(message)}')
    log = open("logs.txt", "a")
    log.write(f'WARNING: {str(message)}\n')
    log.close()

def errorLogger(message):
    #print(f'ERROR: {str(message)}')
    log = open("logs.txt", "a")
    log.write(f'ERROR: {str(message)}\n')
    log.close()