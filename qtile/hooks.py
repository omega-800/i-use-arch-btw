from libqtile import hook
from libqtile.utils import send_notification
from libqtile.log_utils import logger
from libqtile.core.manager import Qtile
import sys
sys.path.insert(0, '/home/omega/.config/themes')
from color_setup import color_setup
"""
@hook.subscribe.client_new
def to_group(window):
    if window.window.get_wm_class() == ['Alacritty', 'Alacritty']:
        window.togroup("1")
    if window.window.get_wm_class() == ['code', 'Code']:
        window.togroup("2")
    if window.window.get_wm_class() == ['qutebrowser', 'qutebrowser']:
        window.togroup("3")
    if window.window.get_wm_class() == ['Navigator', 'firefox']:
        window.togroup("4")
    if window.window.get_wm_class() == ['nuclear', 'nuclear']:
        window.togroup("5")
    window.focus()
"""

@hook.subscribe.startup
def theme_setup():
    color_setup()


#@hook.subscribe.startup_once
#def setup():
#    color_setup()


@hook.subscribe.screen_change
def restart_on_randr(qtile=None):
    send_notification("qtile", "what...")
    # TODO only if numbers of screens changed
    # qtile.cmd_restart()


@hook.subscribe.screens_reconfigured
def restart_on_config(qtile=None):
    send_notification("qtile", "Screen reconfiguration detected.")


"""
@hook.subscribe.startup
def detect_screens():
    while len(screens) < len(qtil.conn.pseudoscreens):
        screens.append(Screen(
            top=bar.Bar([
                widget.GroupBox(
                    disable_drag=True,
                ),
                widget.CurrentLayout(),
            ], 32, ),
        ))
"""