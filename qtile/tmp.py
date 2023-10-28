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
              󰁽  ),
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
        wallpaper='~/documents/img/wallpaper.jpg',
        wallpaper_mode='fill'
    ),
]


