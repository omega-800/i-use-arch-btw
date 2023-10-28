import random
import os
import subprocess

colors = [
    # onedark
    {
        "0": "#282c34",
        "1": "#e06c75",
        "2": "#98c379",
        "3": "#e5c07b",
        "4": "#61afef",
        "5": "#be5046",
        "6": "#56b6c2",
        "7": "#979eab",
        "8": "#393e48",
        "9": "#d19a66",
        "10": "#56b6c2",
        "11": "#e5c07b",
        "12": "#61afef",
        "13": "#be5046",
        "14": "#56b6c2",
        "15": "#abb2bf",
        "fg": "#979eab",
        "bg": "#282c34",
    },
    # Gruvbox
    {
        "0": "#3c3836",
        "1": "#cc241d",
        "2": "#98971a",
        "3": "#d79921",
        "4": "#458588",
        "5": "#b16286",
        "6": "#689d6a",
        "7": "#a89984",
        "8": "#928374",
        "9": "#fb4934",
        "10": "#b8bb26",
        "11": "#fabd2f",
        "12": "#83a598",
        "13": "#d3869b",
        "14": "#8ec07c",
        "15": "#fbf1c7",
        "fg": "#ebdbb2",
        "bg": "#282828",
    },
    # Everforest
    {
        "0": "#343f44",
        "1": "#e67e80",
        "2": "#a7c080",
        "3": "#dbbc7f",
        "4": "#7fbbb3",
        "5": "#d699b6",
        "6": "#83c092",
        "7": "#859289",
        "8": "#3d484d",
        "9": "#e67e80",
        "10": "#a7c080",
        "11": "#dbbc7f",
        "12": "#7fbbb3",
        "13": "#d699b6",
        "14": "#83c092",
        "15": "#9da9a0",
        "fg": "#d3c6aa",
        "bg": "#272e33",
    },
    # Nord
    {
        "0": "#3B4252",
        "1": "#BF616A",
        "2": "#A3BE8C",
        "3": "#EBCB8B",
        "4": "#81A1C1",
        "5": "#B48EAD",
        "6": "#88C0D0",
        "7": "#E5E9F0",
        "8": "#4C566A",
        "9": "#BF616A",
        "10": "#A3BE8C",
        "11": "#EBCB8B",
        "12": "#81A1C1",
        "13": "#B48EAD",
        "14": "#8FBCBB",
        "15": "#ECEFF4",
        "fg": "#d8dee9",
        "bg": "#2e3440",
    },
    # Dracula
    {
        "0": "#21222c",
        "1": "#ff5555",
        "2": "#50fa7b",
        "3": "#f1fa8c",
        "4": "#bd93f9",
        "5": "#ff79c6",
        "6": "#8be9fd",
        "7": "#f8f8f2",
        "8": "#6272a4",
        "9": "#ff6e6e",
        "10": "#69ff94",
        "11": "#ffffa5",
        "12": "#d6acff",
        "13": "#ff92df",
        "14": "#a4ffff",
        "15": "#ffffff",
        "fg": "#f8f8f2",
        "bg": "#282a36",
    }
]

themes = ['onedark', 'gruvbox', 'everforest', 'nord', 'dracula']

themeName = {
    'onedark': 'Arc-Dark',
    'gruvbox': 'gruvbox-dark-gtk',
    'everforest': 'Everforest-Dark-Border',
    'nord': 'Nordic-darker-standard-buttons',
    'dracula': 'Dracula'
}


num = random.randint(0, 4)
theme = themes[num]
curcolors = colors[num]

#os.system("dunstify 'THEME' '" + theme + "'")

#os.system("echo 'include " + theme + ".yml' > ~/.config/alacritty/curr_theme.yml")

#os.system("sed -i 's/^colorscheme .*/colorscheme " + theme + "/' ~/.vimrc")
#command1 = f"sed -i 's/^let g:airline_theme=.*/let g:airline_theme=\"{theme}\"/' ~/.vimrc"
#subprocess.run(command1, shell=True, check=True)

#command2 = f"sed -i 's/^gtk-theme-name=.*/gtk-theme-name=\"{themeName[theme]}\"/' ~/.gtkrc-2.0"
#subprocess.run(command2, shell=True, check=True)
#command3 = "sed -i \"s/^gtk-theme-name=.*/gtk-theme-name=" + themeName[theme] + "/\" ~/.config/gtk-3.0/settings.ini"
#subprocess.run(command3, shell=True, check=True)
