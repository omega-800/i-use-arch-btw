from libqtile.config import Group, Key
from libqtile.lazy import lazy
from libqtile.core.manager import Qtile
from typing import Callable
from keys import keys, mod

groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="1", label="", screen_affinity=0),
    Group(name="2", label="", screen_affinity=0),
    Group(name="3", label="󰇧", screen_affinity=1),
    Group(name="4", label="", screen_affinity=1),
    Group(name="5", label="", screen_affinity=2),
    Group(name="6", label="", screen_affinity=0),
    Group(name="7", label="󰣇", screen_affinity=0),
]


def go_to_group(name: str, switch: bool) -> Callable:
    def _inner(qtile: Qtile) -> None:

        if len(qtile.screens) == 1:
            if switch:
                qtile.current_window.togroup(name, switch_group=True)
            else: 
                qtile.groups_map[name].toscreen()
            return

        if switch:
            qtile.current_window.togroup(name, switch_group=False)

        if len(qtile.screens) == 2:
            if name in '1267':
                qtile.focus_screen(0)
                qtile.groups_map[name].toscreen()
            elif name in '345':
                qtile.focus_screen(1)
                qtile.groups_map[name].toscreen()

        if name in '1267':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        elif name in '34':
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        elif name == '5':
            qtile.focus_screen(2)
            qtile.groups_map[name].toscreen()

    return _inner


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.function(go_to_group(i.name, False)),
                # lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.function(go_to_group(i.name, True)),
                # lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
