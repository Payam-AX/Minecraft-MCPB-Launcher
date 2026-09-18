import core.core as mc

def run():
    z = mc.game()
    res ,log = z.connection_result()
    print(res)
    print(log)
    print("ok")