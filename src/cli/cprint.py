import sys
def cprint(text,end="\n"): 
    if end is None:
        end = ""
    sys.stdout.write(str(text) + end) 
    sys.stdout.flush()