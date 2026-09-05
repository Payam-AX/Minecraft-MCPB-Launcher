import core.check_connection.main as connection_info

class game():
    def __init__(self):
        self.connection = None
        pass
    def connection_result(self):
        self.connection,log = connection_info.connection_info()
        return self.connection,log