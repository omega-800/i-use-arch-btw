import os
import shutil
from current_theme import themes, theme, color_schemes, scheme

replacements = {
    "$THEME_NAME": "catppuccin",
    "$FRAME_COLOR": scheme["highlight"],
    "$FONT_TYPE": "JetBrainsMono Nerd Font Mono",
    "$FONT_SIZE": "10",
    "$LOW_BACKGROUND": scheme["this_current_screen_border"],
    "$LOW_FOREGROUND": scheme["foreground"],
    "$NOR_BACKGROUND": scheme["background"],
    "$NOR_FOREGROUND": scheme["foreground"],
    "$URG_BACKGROUND": scheme["background"],
    "$URG_FOREGROUND": scheme["low_background"],
    "$URG_FRAME": scheme["low_background"],
}


def dunst_setup():
    with open('/home/omega/.config/dunst/dunstrc_template') as infile, open('/home/omega/.config/dunst/dunstrc', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target if src ==
                                    "$FONT_SIZE" else '"'+target+'"')
            outfile.write(line)
    os.system("pkill dunst; /usr/bin/dunst &")


def alacritty_setup():
    with open('/home/omega/.config/alacritty/alacritty_template.yml') as infile, open('/home/omega/.config/alacritty/alacritty.yml', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)


def color_setup():
    dunst_setup()
    alacritty_setup()
    # os.system("sed -i 's/^\(    frame_color = \).*/\1" + scheme["foreground"] + "/' ~/.config/dunst/dunstrc_bak")
    # logger.warn("sed -i 's/^\(    frame_color = \).*/\1\"" + scheme["foreground"] + "\"/' ~/.config/dunst/dunstrc_bak")
    # logger.warn("sed ': label; N; s/[urgency_normal].*\n\(\)//; T label' ~/.config/dunst/dunstrc_bak")
    # logger.warn("cat ~/.config/dunst/dunstrc_bak | tr '\\n' '\\f' | sed 's/\\(\\[urgency_normal\\].*\\f\\)\\(    background = \\).*\\f\\(    foreground = \\).*/\\1\\2\""+scheme["foreground"]+"\"\\n\\3\""+scheme["background"]+"\"/g' | tr '\\f' '\\n' >  ~/.config/dunst/dunstrc_bak")
