import requests, sys, socket
    
try:
    import json
except ImportError:
    import simplejson as json

if not hasattr(socket, "create_connection"):

    def create_connection(address, timeout=None, source_address=None):
        host, port = address

        err = None
        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC,
                                      socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            sock = None
            try:
                sock = socket.socket(af, socktype, proto)

                if timeout is not None:
                    sock.settimeout(timeout)

                if source_address:
                    sock.bind(source_address)

                sock.connect(sa)
                return sock

            except socket.error:
                err = sys.exc_info()[1]
                if sock is not None:
                    sock.close()

        raise err

    socket.create_connection = create_connection

def fetch_json_data(url):
    """Fetch JSON data from the given URL."""
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0"
    }
    response = requests.get(url,headers=headers, timeout=10)
    response.raise_for_status()
    return json.loads(response.content)

def get_json():
    https_urls = [
        "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json",
        "https://piston-meta.mojang.com/mc/game/version_manifest.json",
        "https://launchermeta.mojang.com/mc/game/version_manifest.json",
        "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json",
    ]
    http_urls = [
        "http://piston-meta.mojang.com/mc/game/version_manifest_v2.json",
        "http://piston-meta.mojang.com/mc/game/version_manifest.json",
        "http://launchermeta.mojang.com/mc/game/version_manifest.json",
        "http://launchermeta.mojang.com/mc/game/version_manifest_v2.json",
    ]
    online = True
    log = []
    if sys.version_info[0]==3 or (sys.version_info[0] == 2 and sys.version_info[1] == 7):
        urls = https_urls
    else:
        log.append("fallback to http")
        urls = http_urls
    i=0
    for url in urls:
        i+=1
        try:
            log.append("getting url "+str(i))
            json_data = fetch_json_data(url)
            break
        except:
            log.append("failed to fetch url "+str(i))
            if url == urls[len(urls)-1]:
                    online = False
            continue
    return json_data,online,log