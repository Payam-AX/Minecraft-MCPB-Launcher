import os, requests
import core.core as mc
from core.parse_version import select_version,types

try:
    import json
except ImportError:
    import simplejson as json

try:
    from cli.cprint import cprint
except ImportError:
    from cprint import cprint

try:
    input = raw_input
except NameError:
    pass

def run():
    path_game = "./"
    z = mc.game()
    list_versions, online ,log = z.get_versions_json()
    cprint(online)
    cprint(log)
    cprint("ok")
    available_types = types(list_versions,online)
    
    cprint("Available Types:"+ str(available_types))
    selected_type = ""
    while selected_type not in available_types:
        selected_type = input("Enter your desired type: ").strip()
        if selected_type not in available_types:
            cprint("Invalid type!")
            
    available_versionsintype,log,json_entries = select_version(selected_type,list_versions)
    if available_versionsintype == "":
        cprint(log)
        return
    else:
        cprint(available_versionsintype)
        selected_version = ""
        
        while selected_version not in available_versionsintype:  
            selected_version = input("Enter your desired version: ").strip()
            
            if selected_version not in available_versionsintype:
                cprint("Invalid version!")
        
        
        cprint(selected_version)
        
        if json_entries:
            if not os.path.exists(os.path.normpath(path_game+"./versions/"+selected_version["id"]+"/"+selected_version["id"]+".json")):
                if not os.path.exists(os.path.normpath(path_game+"./versions/"+selected_version["id"])):
                    os.makedirs(os.path.normpath(path_game+"./versions/"+selected_version["id"]))
                selected = [entry for entry in json_entries if entry["id"] == selected_version]
                # print(selected[0]["url"])
                
                response = requests.get(selected[0]["url"])
                response.raise_for_status()
                version = response.json()
                with open(os.path.normpath(path_game+"./versions/"+selected_version["id"]+"/"+selected_version["id"]+".json"), "w") as file:
                    json.dump(version, file, indent=4)
                print(version["id"])