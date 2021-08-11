def infoLogger(message):
    #print(f'INFO: {str(message)}')
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