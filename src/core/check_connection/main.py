import requests


def fetch_json_data(url):
    """Fetch JSON data from the given URL."""
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0"
    }
    response = requests.get(url,headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def connection_info():
    url = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
    url1 = "https://piston-meta.mojang.com/mc/game/version_manifest.json"
    url2 = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    url3 = "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json"
    try:
        print("getting url 1")
        json_data = fetch_json_data(url)
    except:
        print("failed to fetch url 1")
        try:
            print("getting url 2")
            json_data = fetch_json_data(url1)
        except:
            print("failed to fetch url 2")
            try:
                print("getting url 3")
                json_data = fetch_json_data(url2)
            except:
                print("failed to fetch url 3")
                try:
                    print("getting url 4")
                    json_data = fetch_json_data(url3)
                except:
                    print("failed to fetch url 4")
                    offline = True
    return offline