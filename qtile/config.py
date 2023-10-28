# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.core.manager import Qtile
from typing import Callable
from libqtile.log_utils import logger
from colors import curcolors

mod = "mod4"
terminal = guess_terminal()
# terminal = "alacritty"


def shuffle_to_screen(direction: str):
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
    Key([mod], "h", lazy.function(shuffle_to_screen("h")),
        desc="Move focus to left"),
    Key([mod], "l", lazy.function(shuffle_to_screen("l")), desc="Move focus to right"),
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
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([mod, "control"], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn("qutebrowser"), desc="Spawn browser"),
    Key([mod], "m", lazy.spawn("nuclear"), desc="Spawn music player"),
]

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

layouts = [
    layout.Columns(
        border_focus=curcolors['fg'],
        border_normal=curcolors['bg'],
        border_focus_stack=[curcolors['fg'], curcolors['bg']],
        border_width=4,
        margin=8,
        margin_on_single=8,
        border_on_single=True
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        bg_color=curcolors['bg'],
        inactive_fg=curcolors['fg'],
        inactive_bg=curcolors['0'],
        active_fg=curcolors['bg'],
        active_bg=curcolors['2'],
        font="JetBrainsMono Nerd Font Mono",
        fontsize=18,
        padding=6,
        section_fontsize=14,
        section_padding=4,
        section_fg=curcolors['fg']
    ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="sans",
    font="JetBrainsMono Nerd Font Mono",
    fontsize=18,
    padding=6,
    foreground=curcolors['bg'],
    background=curcolors['bg']
)
extension_defaults = widget_defaults.copy()
font_ic = 22
text_ic = '󱎕'
screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(foreground=curcolors['fg']),
                widget.GroupBox(
                    background=curcolors['bg'],
                    foreground=curcolors['fg'],
                    highlight_method='line',
                    active=curcolors['bg'],
                    inactive=curcolors['fg'],
                    highlight_color=[curcolors['fg'], curcolors['fg']],
                    this_current_screen_border=curcolors['4'],
                    this_screen_border=curcolors['5'],
                ),
                widget.Prompt(
                    foreground=curcolors['fg']
                ),
                widget.WindowName(
                    foreground=curcolors['fg']
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.TextBox(
                    text=text_ic,
                    foreground=curcolors['6'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.Net(
                    background=curcolors['6'],
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                ),
                widget.DF(
                    background=curcolors['1'],
                    visible_on_warn=True,
                    warn_space=2
                ),
                widget.TextBox(
                    text=text_ic,
                    background=curcolors['6'],
                    foreground=curcolors['5'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.Memory(
                    background=curcolors['5'],
                    measure_mem='G',
                ),
                widget.TextBox(
                    text=text_ic,
                    background=curcolors['5'],
                    foreground=curcolors['3'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.CPU(
                    background=curcolors['3'],
                    format=' {load_percent}%',
                ),
                widget.TextBox(
                    text=text_ic,
                    background=curcolors['3'],
                    foreground=curcolors['1'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.Volume(
                    background=curcolors['1'],
                    emoji=True,
                    emoji_list=['󰖁', '󰝞', '󰖀', '󰕾']
                ),
                widget.TextBox(
                    text=text_ic,
                    background=curcolors['1'],
                    foreground=curcolors['2'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.Battery(
                    background=curcolors['2'],
                    format='{char}{percent:2.0%}',
                    low_background=curcolors['fg'],
                    low_percentage=0.4,
                    notify_below=0.3,
                    charge_char='󱐋',
                    discharge_char='',
                    empty_char='󰁺',
                    full_char='󰁹',
                    not_charging_char='',
                    unknown_char='󰂑'
                ),
                widget.TextBox(
                    text=text_ic,
                    background=curcolors['2'],
                    foreground=curcolors['4'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.Clock(
                    format="%H:%M 󰥔 %d.%m.%y",
                    background=curcolors['4']
                ),
                widget.TextBox(
                    text=text_ic,
                    background=curcolors['4'],
                    foreground=curcolors['7'],
                    padding=0,
                    fontsize=font_ic
                ),
                widget.Wttr(
                    location={'Zurich': 'Home'},
                    format="%c%t",
                    background=curcolors['7'],
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        wallpaper='~/img/wallpaper.jpg',
        wallpaper_mode='stretch'
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
