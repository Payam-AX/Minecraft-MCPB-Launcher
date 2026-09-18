import core.core as mc
try:
    from cli.select_version import select_version
except ImportError:
    from select_version import select_version


def run():
    z = mc.game()
    list_versions, online ,log = z.get_versions_json()
    print(online)
    print(log)
    print("ok")
    select_version(list_versions,online)