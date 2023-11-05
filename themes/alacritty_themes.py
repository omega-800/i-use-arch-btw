from libqtile.log_utils import logger
from os import listdir, path
import yaml, re, subprocess
from shutil import copyfile

curr_theme_path = '/home/omega/.config/themes/current_theme.yaml'
themes_path = '/home/omega/.config/alacritty/themes/themes'
theme_paths = (themes_path+"2/"+f for f in listdir(themes_path+"2") if f.endswith(".yml"))
theme_paths2 = (themes_path+"/"+f for f in listdir(themes_path) if f.endswith(".yaml"))

all_themes = dict()

for theme in theme_paths:
    all_themes[re.sub(".*/(.*)\\.yml", "\\1", theme)] = theme

# ({re.sub("(.*)\\.yml", "\\1", f),themes_path+"2/"+f} for f in listdir(themes_path+"2") if f.endswith(".yml"))

def get_themes():
    return list(re.sub("(.*)\\.yml", "\\1", f) for f in listdir(themes_path+"2") if f.endswith(".yml"))


def get_colors():
    with open(curr_theme_path) as stream:
        return yaml.safe_load(stream)['colors']


def set_colors(theme_name: str):
    if theme_name == "random": theme_name = choice(get_themes())
    subprocess.run("dunstify 'theme' '"+theme_name+"'", shell=True)
    if not theme_name in get_themes(): theme_name = 'catppuccin-mocha'
    copyfile(all_themes[theme_name], curr_theme_path)
    with open(curr_theme_path, 'a') as file:
        file.write("  name: '"+theme_name+"'")
    
