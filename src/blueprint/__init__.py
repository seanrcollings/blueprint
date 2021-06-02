from i3ipc import Connection
from arc import CLI

wm = Connection()

root = wm.get_tree()
