from libqtile import bar, widget, qtile
from libqtile.config import Screen
from curcolors import curcolors

theme = dict(
    base03='#002b36',
    base02='#073642',
    base01='#586e75',
    base00='#657b83',
    base0='#839496',
    base1='#93a1a1',
    base2='#eee8d5',
    base3='#fdf6e3',
    yellow='#b58900',
    orange='#cb4b16',
    red='#dc322f',
    magenta='#d33682'
)

color_schemes = [
    dict(
        background=colors.colors['catppuccin']['nor_red'],
        foreground=theme['base1']
    ),
    dict(
        background=theme['base3'],
        foreground=theme['base02']
    )
]

# "","","","",
# 󱩅


def separator(left_looking=True):
    global color_scheme
    if left_looking:
        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return widget.TextBox(
            **separator_defaults,
            text="",
            foreground=color_scheme["background"],
            background=color_scheme["foreground"]
        )
    else:
        ret = widget.TextBox(
            **separator_defaults,
            text="",
            foreground=color_scheme["background"],
            background=color_scheme["foreground"]
        )

        separator.current_scheme = 1 - separator.current_scheme
        color_scheme = color_schemes[separator.current_scheme]

        return ret


color_scheme = color_schemes[1]
separator.current_scheme = 1

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
        active=curcolors['bg'],
        inactive=curcolors['fg'],
        highlight_color=[curcolors['fg'], curcolors['fg']],
        this_current_screen_border=curcolors['4'],
        this_screen_border=curcolors['5'],
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
