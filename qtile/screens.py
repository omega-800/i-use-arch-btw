from libqtile import bar, widget, qtile
from libqtile.config import Screen
import sys
from libqtile.core.manager import Qtile
from libqtile.log_utils import logger
sys.path.insert(0, '/home/omega/.config/themes')
from alacritty_themes import get_colors
from random import randint

theme = get_colors()['colors']
color_schemes = []
i=0
for shade in [theme['bright'], theme['normal']]:
    color_schemes.append(dict(
        background=theme["primary"]["background" if i == 0 else "foreground"],
        foreground=theme["primary"]["background" if i == 1 else "foreground"],
        active=theme['cursor']['cursor'],
        inactive=theme['selection']['background'],
        highlight_color=[theme['primary']['background'],
                            theme['primary']['background']],
        highlight=theme['primary']['background'],
        this_current_screen_border=shade['magenta'],
        this_screen_border=shade['blue'],
        low_background=shade['red'],
    ))
    i+=1

scheme_i = 0 #randint(0, 1)
scheme = color_schemes[scheme_i]


# "","","","",

def separator(left_looking=True):
    global color_scheme
    if left_looking:
        background = color_schemes[separator.current_scheme]["background"]
        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return widget.TextBox(
            **separator_defaults,
            text="",
            foreground=color_scheme["background"],
            background=background
        )
    else:
        background = color_schemes[1 - separator.current_scheme]["background"]

        ret = widget.TextBox(
            **separator_defaults,
            text="",
            foreground=color_scheme["background"],
            background=background
        )

        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return ret


separator.current_scheme = scheme_i
color_scheme = color_schemes[separator.current_scheme]

# u'\ue0b0',
separator_defaults = dict(
    font='JetBrainsMono Nerd Font Mono',
    fontsize=26,
    padding=0,
)

widget_defaults = dict(
    font='JetBrainsMono Nerd Font Mono',
    fontsize=16,
    padding=6,
)
extension_defaults = widget_defaults.copy()

icon_defaults = dict(
    font='feather',
    fontsize=16,
    padding=6,
)

battery_widget_defaults = dict(
    format='{char}[{percent:2.0%}]  ',
    low_percentage=0.4,
    update_interval=5,
    notify_below=0.3,
    charge_char='󱐋',
    discharge_char='󰁽',
    empty_char='󰁺',
    full_char='󰁹',
    not_charging_char='',
    unknown_char='󰂑'
)

bar_widgets = [
    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
        highlight_method='line',
    ),
    separator(left_looking=False),
    widget.Prompt(
        **widget_defaults,
        **color_scheme,
    ),
    widget.WindowName(
        **widget_defaults,
        **color_scheme,
    ),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    # widget.StatusNotifier(),
    widget.Systray(
        icon_size=20,
        **widget_defaults,
        **color_scheme,
    ),
    separator(),
    widget.Net(
        **widget_defaults,
        **color_scheme,
        format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
    ),
    widget.DF(
        **widget_defaults,
        **color_scheme,
        visible_on_warn=True,
        warn_space=2
    ),
    separator(),
    widget.Memory(
        **widget_defaults,
        **color_scheme,
        measure_mem='G',
    ),
    separator(),
    widget.CPU(
        **widget_defaults,
        **color_scheme,
        format=' {load_percent}%',
    ),
    separator(),
    #widget.Wttr(
    #    **widget_defaults,
    #    **color_scheme,
    #    location={'Zurich': 'Home'},
    #    format="%c%t",
    #),
    #separator(),
    widget.Battery(
        **widget_defaults,
        **color_scheme,
        format='{char}{percent:2.0%}',
        low_percentage=0.4,
        notify_below=0.3,
        charge_char='󱐋',
        discharge_char='',
        empty_char='󰁺',
        full_char='󰁹',
        not_charging_char='',
        unknown_char='󰂑'
    ),
    separator(),
    widget.Volume(
        **widget_defaults,
        **color_scheme,
        emoji=True,
        emoji_list=['󰖁', '󰝞', '󰖀', '󰕾']
    ),
    separator(),
    widget.Clock(
        **widget_defaults,
        **color_scheme,
        format="%H:%M 󰥔 %d.%m.%y",
    ),
]

# Second screen bar
separator.current_scheme = 0

second_bar_widgets = [
    widget.GroupBox(
        **widget_defaults,
        **color_scheme,
    ),
    separator(),
    widget.Spacer(
        length=16,
        **color_scheme,
    ),
    widget.WindowName(
        **widget_defaults,
        **color_scheme,
    ),
    separator(left_looking=False),
    widget.CurrentScreen(
        **widget_defaults,
        **color_scheme,
        active_text="active",
        inactive_text="inactive"
    ),
]

screens = [
    Screen(
        top=bar.Bar(
            bar_widgets,
            24,
        ),
        wallpaper='~/documents/img/wallpaper.jpg',
        wallpaper_mode='fill'
    ),
]

if len(qtile.screens) > 1:
    logger.warn(len(qtile.screens))
    for i in range(1, len(qtile.screens)):
        screens.append(
            Screen(
                bottom=bar.Bar(
                    bar_widgets,
                    24,
                ),
                wallpaper='~/documents/img/wallpaper.jpg',
                wallpaper_mode='fill'
            )
        )

