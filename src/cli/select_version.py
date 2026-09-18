import os
try:
    from cli.cprint import cprint
except ImportError:
    from cprint import cprint
    
try:
    input = raw_input
except NameError:
    pass


def extract_unique_types(data):
    """Extract unique types from JSON entries."""
    return sorted(set(entry["type"] for entry in data))

def filter_by_type(data, selected_type):
    """Filter JSON entries based on selected type."""
    return [entry for entry in data if entry["type"] == selected_type]

def select_version(json_data,online,path_game = "./"):
    existing_types = []
    # Extract types
    existing_types.append('installed')
    if online:
        existing_types.append('latest_release')
        existing_types.append('latest_snapshot')
        for z in extract_unique_types(json_data["versions"]):
            existing_types.append(z)
    cprint("Available Types:"+ str(existing_types))

    # Let the user select a type
    selected_type = ""
    
    while selected_type not in existing_types:
        selected_type = input("Enter your desired type: ").strip()
    # if selected_type not in existing_types:
    #     print("Invalid type selected!")
    #     return
    
    filtered_entries = False
    
    if selected_type.lower() == "installed":
        existing_versions = []
        if os.path.exists(os.path.normpath(path_game+"./versions/")):
            for i in(os.listdir(os.path.normpath(path_game+"./versions/"))):
                if os.path.exists(os.path.normpath(path_game+"./versions/"+i+"/"+i+".json")):
                    existing_versions.append(i)
            cprint(existing_versions)
        else:
            cprint("no installed versions detected!")
            return
    elif selected_type.lower() == "latest_release":
        existing_versions = [json_data["latest"]["release"]]
        filtered_entries = filter_by_type(json_data["versions"], "release")
        cprint(existing_versions)
    elif selected_type.lower() == "latest_snapshot":
        existing_versions = [json_data["latest"]["snapshot"]]
        filtered_entries = filter_by_type(json_data["versions"], "snapshot")
        cprint(existing_versions)
    else:
        # Filter and display matching entries
        filtered_entries = filter_by_type(json_data["versions"], selected_type)
        cprint("\nEntries for ''"+selected_type+"'': ")
        # json.dumps(filtered_entries, indent=4)
        existing_versions = sorted(set(entry["id"] for entry in filtered_entries))
        cprint(existing_versions)
    
    selected_type1 = ""
    
    while selected_type1 not in existing_versions:  
        selected_type1 = input("Enter your desired version: ").strip()
    
    return selected_type1