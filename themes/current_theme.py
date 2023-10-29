from random import randint
from themes.catppuccin_latte import catppuccin_latte as latte
from themes.catppuccin_mocha import catppuccin_mocha as mocha
from themes.catppuccin_frappe import catppuccin_frappe as frappe
from themes.catppuccin_macchiato import catppuccin_macchiato as macchiato
from libqtile.log_utils import logger

themes = [latte, macchiato, mocha, frappe]
theme = themes[3]
#theme = themes[randint(0, 3)]

color_schemes = [
    dict(
        background=theme["base"],
        foreground=theme["subtext0"],
        active=theme['text'],
        inactive=theme['subtext1'],
        highlight_color=[theme['overlay0'], theme['overlay0']],
        highlight=theme['overlay0'],
        this_current_screen_border=theme['lavender'],
        this_screen_border=theme['blue'],
        low_background=theme['red'],
    ),
    dict(
        background=theme["crust"],
        foreground=theme["subtext1"],
        active=theme['subtext0'],
        inactive=theme['overlay2'],
        highlight_color=[theme['surface2'], theme['surface2']],
        highlight=theme['surface2'],
        this_current_screen_border=theme['rosewater'],
        this_screen_border=theme['peach'],
        low_background=theme['red'],
    )
]

scheme_i = randint(0, 1)
scheme = color_schemes[scheme_i]

