import os, sys, subprocess, shutil
from alacritty_themes import get_colors, set_colors, get_themes, get_replacements
from random import randint, choice
from libqtile.log_utils import logger
from libqtile.core.manager import Qtile

def dunst_setup(replacements):
    with open('/home/omega/.config/dunst/dunstrc_template') as infile, open('/home/omega/.config/dunst/dunstrc', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target if src == "$FONT_SIZE" else '"'+target+'"')
            outfile.write(line)
    os.system("pkill dunst; /usr/bin/dunst &")


def alacritty_setup(replacements):
    with open('/home/omega/.config/alacritty/alacritty_template.yml') as infile, open('/home/omega/.config/alacritty/alacritty.yml', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)


def rofi_setup(replacements):
    with open('/home/omega/.config/rofi/themes/current_theme_template.rasi') as infile, open('/home/omega/.config/rofi/themes/current_theme.rasi', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)

# def qutebrowser_setup():
    # os.system("pkill qutebrowser; /usr/bin/qutebrowser &")


def color_setup():
    replacements = get_replacements()
    dunst_setup(replacements)
    alacritty_setup(replacements)
    rofi_setup(replacements)
    #subprocess.run('qtile cmd-obj -o cmd -f reload_config', shell=True)

# os.system("sed -i 's/^\(    frame_color = \).*/\1" + scheme["foreground"] + "/' ~/.config/dunst/dunstrc_bak")
# logger.warn("sed -i 's/^\(    frame_color = \).*/\1\"" + scheme["foreground"] + "\"/' ~/.config/dunst/dunstrc_bak")
# logger.warn("sed ': label; N; s/[urgency_normal].*\n\(\)//; T label' ~/.config/dunst/dunstrc_bak")
# logger.warn("cat ~/.config/dunst/dunstrc_bak | tr '\\n' '\\f' | sed 's/\\(\\[urgency_normal\\].*\\f\\)\\(    background = \\).*\\f\\(    foreground = \\).*/\\1\\2\""+scheme["foreground"]+"\"\\n\\3\""+scheme["background"]+"\"/g' | tr '\\f' '\\n' >  ~/.config/dunst/dunstrc_bak")


#if len(sys.argv) > 1:
#    set_colors(theme_name=sys.argv[1])

