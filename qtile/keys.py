
from libqtile.lazy import lazy
from libqtile.core.manager import Qtile
from libqtile.utils import guess_terminal
from libqtile.config import Click, Drag, Key, KeyChord
import os, sys, subprocess
sys.path.insert(0, '/home/omega/.config/themes')
from alacritty_themes import get_themes, set_colors
from libqtile.log_utils import logger

terminal = guess_terminal()
# terminal = "alacritty"
mod = "mod4"


@lazy.function
def screenshot(qtile):
    os.system('maim /home/omega/documents/img/screenshots/$(date +%s).png')


@lazy.function
def theme(qtile):
    options = '\n'.join(get_themes())
    selected = os.popen('printf "'+options+'" | rofi -dmenu').read().replace('\n','')
    set_colors(selected)

def focus_to_screen(direction: str):
    def _inner(qtile: Qtile) -> None:
        lcur = qtile.current_layout.info()["current"]
        lmax = len(qtile.current_layout.info()["columns"]) - 1
        scur = qtile.screens.index(qtile.current_screen)
        smax = len(qtile.screens) - 1
        if direction == "h":
            if len(qtile.screens) > 1 and lcur == 0:
                qtile.focus_screen(scur - 1 if scur > 0 else smax)
            else:
                qtile.current_layout.left()
        if direction == "l":
            if len(qtile.screens) > 1 and lcur == lmax:
                qtile.focus_screen(scur + 1 if scur < smax else 0)
            else:
                qtile.current_layout.right()
        if direction == "j":
            lazy.layout.down()
        if direction == "k":
            lazy.layout.up()
    return _inner


@lazy.function
def spawn_to_group(qtile, client, group):
    qtile.groups_map[group].toscreen()
    qtile.spawn(client)


def switch_screens(qtile):
    if len(qtile.screens) == 1:
        previous_switch = getattr(qtile, "previous_switch", None)
        qtile.previous_switch = qtile.current_group
        return qtile.current_screen.toggle_group(previous_switch)

    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod, "control"], "t", lazy.function(switch_screens)),
    Key([mod], "h", lazy.function(focus_to_screen("h")),
        desc="Move focus to left"),
    Key([mod], "l", lazy.function(focus_to_screen("l")),
        desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtiqle"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "b",
        lazy.hide_show_bar(),
        desc="Toggle qtile bar",
        ),
    Key([mod], "g", lazy.togroup()),
    Key([mod, "shift"], "s", screenshot),
    Key([mod, "shift"], "t", theme),
    Key([mod], "x", lazy.spawn("slock"), desc="Lock screen"),
    KeyChord([mod], "s", [
        Key([], "s", lazy.spawn("rofi -show drun"), desc="Select app"),
        Key([], "m", spawn_to_group("minecraft-launcher","1"), desc="Spawn minecraft"),
        Key([], "o", spawn_to_group("obsidian", "1"), desc="Spawn obsidian"),
        Key([], "c", spawn_to_group("code","2"), desc="Spawn VS Code"),
        Key([], "v", spawn_to_group("alacritty -e nvim", "2"), desc="Spawn Vim"),
        Key([], "b", spawn_to_group("qutebrowser", "3"), desc="Spawn browser"),
        Key([], "f", spawn_to_group("firefox","3"), desc="Spawn Firefox"),
        Key([], "d", spawn_to_group("discord","4"), desc="Spawn discord"),
        Key([], "e", spawn_to_group("alacritty -e aerc", "4"), desc="Spawn Email"),
        Key([], "n", spawn_to_group("alacritty -e ncmpcpp","5"), desc="Spawn music player"),
        Key([], "r", spawn_to_group("renoise", "5"), desc="Spawn tracker"),
        Key([], "x", spawn_to_group("alacritty -e lf", "6"), desc="Spawn file explorer"),
        Key([], "l", spawn_to_group("libreoffice", "6"), desc="Spawn libre office"),
        Key([], "h", spawn_to_group("homebank", "7"), desc="Spawn finance app"),
    ],
        name="Spawn"
    ),
    KeyChord([mod], "n", [
        Key([], "k", lazy.spawn("mpc prev")),
        Key([], "j", lazy.spawn("mpc next")),
        Key([], "l", lazy.spawn("mpc seek + 00:00:05")),
        Key([], "h", lazy.spawn("mpc seek - 00:00:05")),
        Key([], "p", lazy.spawn("mpc toggle")),
        Key([], "s", lazy.spawn("mpc random")),
        Key([], "r", lazy.spawn("mpc repeat")),
    ],
        name="Music"
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
