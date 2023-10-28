from libqtile.config import Group, Key
from libqtile.lazy import lazy
from libqtile.core.manager import Qtile
from typing import Callable
from keys import keys, mod

groups = [
    # Screen affinity here is used to make
    # sure the groups startup on the right screens
    Group(name="1", screen_affinity=0),
    Group(name="2", screen_affinity=0),
    Group(name="3", screen_affinity=0),
    Group(name="4", screen_affinity=0),
    Group(name="q", screen_affinity=1),
    Group(name="w", screen_affinity=1),
    Group(name="e", screen_affinity=1),
    Group(name="a", screen_affinity=2),
    Group(name="s", screen_affinity=2),
]


def go_to_group(name: str, switch: bool) -> Callable:
    def _inner(qtile: Qtile) -> None:

        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            if switch:
                qtile.current_window.togroup(name, switch_group=True)
            return

        if switch:
            qtile.current_window.togroup(name, switch_group=False)

        if len(qtile.screens) == 2:
            if name in '1234as':
                qtile.focus_screen(0)
                qtile.groups_map[name].toscreen()
            elif name in 'qwe':
                qtile.focus_screen(1)
                qtile.groups_map[name].toscreen()

        if name in '1234':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        elif name in 'qwe':
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        elif name in 'as':
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
