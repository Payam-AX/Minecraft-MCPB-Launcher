import core.check_connection.main as connection_info

class game():
    def __init__(self,connection):
        self.connection = connection
        pass
    def connection_result(self):
        self.connection = connection_info.isonline