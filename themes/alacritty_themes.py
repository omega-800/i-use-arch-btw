from libqtile.log_utils import logger
from os import listdir, path
import yaml
import re

themes_path = '/home/omega/.config/alacritty/themes/themes'
theme_paths = (themes_path+"2/"+f
               for f in listdir(themes_path+"2") if f.endswith(".yml"))
theme_paths2 = (themes_path+"/"+f
                for f in listdir(themes_path) if f.endswith(".yaml"))

all_themes = dict()

for theme in theme_paths:
    all_themes[re.sub(".*/(.*)\\.yml", "\\1", theme)] = theme


def get_colors(theme_name: str):
    if not theme_name in all_themes.values(): theme_name = 'catppuccin-mocha'
    with open(all_themes[theme_name], 'r') as stream:
        dict = yaml.safe_load(stream)
        print(yaml.dump(dict))
        return dict

