import os
import shutil
from current_theme import color_schemes
from alacritty_themes import get_colors
import sys
from random import randint

scheme_i = randint(0,1)
scheme = color_schemes[scheme_i]

def dunst_setup(theme, replacements):
    with open('/home/omega/.config/dunst/dunstrc_template') as infile, open('/home/omega/.config/dunst/dunstrc', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target if src ==
                                    "$FONT_SIZE" else '"'+target+'"')
            outfile.write(line)
    os.system("pkill dunst; /usr/bin/dunst &")


def alacritty_setup(theme, replacements):
    with open('/home/omega/.config/alacritty/alacritty_template.yml') as infile, open('/home/omega/.config/alacritty/alacritty.yml', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

# def qutebrowser_setup():
    # os.system("pkill qutebrowser; /usr/bin/qutebrowser &")


def color_setup(theme_name="catppuccin-mocha"):
    global scheme, scheme_i, color_schemes
    theme = get_colors(theme_name)['colors']
    color_schemes = []
    for shade in [theme['bright'], theme['normal']]:
        color_schemes.append(dict(
            background=shade["black"],
            foreground=shade["white"],
            active=theme['cursor']['text'],
            inactive=theme['selection']['text'],
            highlight_color=[theme['primary']['foreground'],
                             theme['primary']['foreground']],
            highlight=theme['primary']['foreground'],
            this_current_screen_border=shade['magenta'],
            this_screen_border=shade['blue'],
            low_background=shade['red'],
        ))
    scheme_i = randint(0, 1)
    scheme = color_schemes[scheme_i]
    print(theme_name)
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
    print(scheme)
    print(replacements)
    dunst_setup(theme, replacements)
    alacritty_setup(theme, replacements)


# os.system("sed -i 's/^\(    frame_color = \).*/\1" + scheme["foreground"] + "/' ~/.config/dunst/dunstrc_bak")
# logger.warn("sed -i 's/^\(    frame_color = \).*/\1\"" + scheme["foreground"] + "\"/' ~/.config/dunst/dunstrc_bak")
# logger.warn("sed ': label; N; s/[urgency_normal].*\n\(\)//; T label' ~/.config/dunst/dunstrc_bak")
# logger.warn("cat ~/.config/dunst/dunstrc_bak | tr '\\n' '\\f' | sed 's/\\(\\[urgency_normal\\].*\\f\\)\\(    background = \\).*\\f\\(    foreground = \\).*/\\1\\2\""+scheme["foreground"]+"\"\\n\\3\""+scheme["background"]+"\"/g' | tr '\\f' '\\n' >  ~/.config/dunst/dunstrc_bak")


if len(sys.argv) > 1:
    color_setup(theme_name=sys.argv[1])
