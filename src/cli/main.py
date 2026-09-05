import core.main as mc

def run():
    z = mc.game()
    res ,log = z.connection_result()
    print(res)
    print(log[len(log)-1])
    print("ok")