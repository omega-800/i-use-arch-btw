import os
import shutil
from alacritty_themes import get_colors, set_colors, all_themes
import sys
from random import randint, choice
from libqtile.log_utils import logger

def dunst_setup(replacements):
    with open('/home/omega/.config/dunst/dunstrc_template') as infile, open('/home/omega/.config/dunst/dunstrc', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target if src ==
                                    "$FONT_SIZE" else '"'+target+'"')
            outfile.write(line)
    os.system("pkill dunst; /usr/bin/dunst &")


def alacritty_setup(replacements):
    with open('/home/omega/.config/alacritty/alacritty_template.yml') as infile, open('/home/omega/.config/alacritty/alacritty.yml', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

# def qutebrowser_setup():
    # os.system("pkill qutebrowser; /usr/bin/qutebrowser &")

def color_setup(theme_name="random"):
    global scheme, scheme_i, color_schemes
    if theme_name == "random": 
        theme_name = choice(list(all_themes.keys()))
    set_colors(theme_name)
    os.system("dunstify 'theme' "+theme_name)
    theme = get_colors()
    color_schemes = []
    for shade in [theme['bright'], theme['normal']]:
        color_schemes.append(dict(
            background=shade["black"],
            foreground=shade["white"],
            active=theme['cursor']['text'],
            inactive=theme['selection']['text'],
            highlight_color=[theme['primary']['background'],
                             theme['primary']['background']],
            highlight=theme['primary']['background'],
            this_current_screen_border=shade['magenta'],
            this_screen_border=shade['blue'],
            low_background=shade['red'],
        ))
    scheme_i = 0 #randint(0, 1)
    scheme = color_schemes[scheme_i]
    replacements = {
        "$THEME_NAME": theme_name,
        "$FRAME_COLOR": scheme["highlight"],
        "$FONT_TYPE": "JetBrainsMono Nerd Font Mono",
        "$FONT_SIZE": "10",
        "$LOW_BACKGROUND": scheme["this_current_screen_border"],
        "$LOW_FOREGROUND": scheme["foreground"],
        "$LOW_HIGHLIGHT": scheme["active"],
        "$NOR_BACKGROUND": scheme["background"],
        "$NOR_FOREGROUND": scheme["foreground"],
        "$NOR_HIGHLIGHT": scheme["active"],
        "$CRI_BACKGROUND": scheme["background"],
        "$CRI_FOREGROUND": scheme["low_background"],
        "$CRI_FRAME": scheme["low_background"],
        "$CRI_HIGHLIGHT": scheme["active"],
    }
    dunst_setup(replacements)
    alacritty_setup(replacements)


# os.system("sed -i 's/^\(    frame_color = \).*/\1" + scheme["foreground"] + "/' ~/.config/dunst/dunstrc_bak")
# logger.warn("sed -i 's/^\(    frame_color = \).*/\1\"" + scheme["foreground"] + "\"/' ~/.config/dunst/dunstrc_bak")
# logger.warn("sed ': label; N; s/[urgency_normal].*\n\(\)//; T label' ~/.config/dunst/dunstrc_bak")
# logger.warn("cat ~/.config/dunst/dunstrc_bak | tr '\\n' '\\f' | sed 's/\\(\\[urgency_normal\\].*\\f\\)\\(    background = \\).*\\f\\(    foreground = \\).*/\\1\\2\""+scheme["foreground"]+"\"\\n\\3\""+scheme["background"]+"\"/g' | tr '\\f' '\\n' >  ~/.config/dunst/dunstrc_bak")


if len(sys.argv) > 1:
    color_setup(theme_name=sys.argv[1])
