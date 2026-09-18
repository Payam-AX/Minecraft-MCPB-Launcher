import core.core as mc
from core.parse_version import select_version,types

try:
    from cli.cprint import cprint
except ImportError:
    from cprint import cprint

try:
    input = raw_input
except NameError:
    pass

def run():
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
            
    available_versionsintype,log = select_version(selected_type,list_versions)
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