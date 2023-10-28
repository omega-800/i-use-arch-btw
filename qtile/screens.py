from libqtile import bar, widget, qtile
from libqtile.config import Screen
from random import randint
from themes.catppuccin_latte import catppuccin_latte as latte
from themes.catppuccin_macchiato import catppuccin_macchiato as macchiato
from themes.catppuccin_mocha import catppuccin_mocha as mocha
from themes.catppuccin_frappe import catppuccin_frappe as frappe
from libqtile.log_utils import logger

themes = [latte, macchiato, mocha, frappe]

theme = themes[randint(0,3)] 

logger.warn(theme['maroon'])
color_schemes = [
    dict(
        background=theme["maroon"],
        foreground=theme["base"],
        active=theme['base'],
        inactive=theme['rosewater'],
        highlight_color=[theme['maroon'], theme['maroon']],
        this_current_screen_border=theme['peach'],
        this_screen_border=theme['pink'],
        low_background=theme['red'],
    ),
    dict(
        background=theme["lavender"],
        foreground=theme["text"],
        active=theme['text'],
        inactive=theme['overlay0'],
        highlight_color=[theme['lavender'], theme['lavender']],
        this_current_screen_border=theme['mauve'],
        this_screen_border=theme['sky'],
        low_background=theme['yellow'],
    )
]

# "","","","",
# 󱩅


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


separator.current_scheme = randint(0,1) 
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
    widget.StatusNotifier(),
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
    widget.Volume(
        **widget_defaults,
        **color_scheme,
        emoji=True,
        emoji_list=['󰖁', '󰝞', '󰖀', '󰕾']
    ),
    separator(),
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
    widget.Clock(
        **widget_defaults,
        **color_scheme,
        format="%H:%M 󰥔 %d.%m.%y",
    ),
    separator(),
    widget.Wttr(
        **widget_defaults,
        **color_scheme,
        location={'Zurich': 'Home'},
        format="%c%t",
    )
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
        bottom=bar.Bar(
            bar_widgets,
            24,
        ),
        wallpaper='~/documents/img/wallpaper.jpg',
        wallpaper_mode='fill'
    ),
]

if len(qtile.screens) > 1:
    for i in range(2, len(qtile.screens)):
        screens.append(
            Screen(
                top=bar.Bar(
                    second_bar_widgets,
                    24,
                ),
                wallpaper='~/documents/img/wallpaper.jpg',
                wallpaper_mode='fill'
            )
        )
