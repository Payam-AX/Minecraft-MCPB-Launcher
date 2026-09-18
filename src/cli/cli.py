import core.core as mc
try:
    from cli.select_version import select_version
except ImportError:
    from select_version import select_version

try:
    from cli.cprint import cprint
except ImportError:
    from cprint import cprint

def run():
    z = mc.game()
    list_versions, online ,log = z.get_versions_json()
    cprint(online)
    cprint(log)
    cprint("ok")
    selected_version = select_version(list_versions,online)
    cprint(selected_version)