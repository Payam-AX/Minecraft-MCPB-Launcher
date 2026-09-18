try:
    import core.get_versions_json as get_json
except ImportError:
    import get_versions_json as get_json

class game():
    def __init__(self):
        self.connection_status = None
        pass
    def get_versions_json(self):
        version_json,self.connection_status,log = get_json.get_json()
        return version_json,self.connection_status,log