import sys
def cprint(text,end=""): 
    if end != None:
        end = "\n"
    sys.stdout.write(str(text) + end) 
    sys.stdout.flush()