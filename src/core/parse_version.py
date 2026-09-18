import os
    


def extract_unique_types(data):
    """Extract unique types from JSON entries."""
    return sorted(set(entry["type"] for entry in data))

def filter_by_type(data, selected_type):
    """Filter JSON entries based on selected type."""
    return [entry for entry in data if entry["type"] == selected_type]

def types(json_data,online,path_game = "./"):
    existing_types = []
    # Extract types
    existing_types.append('installed')
    if online:
        existing_types.append('latest_release')
        existing_types.append('latest_snapshot')
        for z in extract_unique_types(json_data["versions"]):
            existing_types.append(z)
            
    return existing_types

def select_version(selected_type,json_data,path_game = "./"):
    log=[]
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
        else:
            log.append("no installed versions detected!")
            return "",log
    elif selected_type.lower() == "latest_release":
        existing_versions = [json_data["latest"]["release"]]
        filtered_entries = filter_by_type(json_data["versions"], "release")
        # cprint(existing_versions)
    elif selected_type.lower() == "latest_snapshot":
        existing_versions = [json_data["latest"]["snapshot"]]
        filtered_entries = filter_by_type(json_data["versions"], "snapshot")
        # cprint(existing_versions)
    else:
        # Filter and display matching entries
        filtered_entries = filter_by_type(json_data["versions"], selected_type)
        # cprint("\nEntries for ''"+selected_type+"'': ")
        # json.dumps(filtered_entries, indent=4)
        existing_versions = sorted(set(entry["id"] for entry in filtered_entries))
        # cprint(existing_versions)
    
    return existing_versions,log