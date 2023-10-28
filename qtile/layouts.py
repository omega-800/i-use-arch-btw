from libqtile import layout
from libqtile.config import Match
from config import curcolors

layouts = [
    layout.Columns(
        border_focus=curcolors['fg'],
        border_normal=curcolors['0'],
        border_focus_stack=[curcolors['fg'], curcolors['bg']],
        border_width=4,
        margin=8,
        margin_on_single=8,
        border_on_single=True
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        bg_color=curcolors['bg'],
        inactive_fg=curcolors['fg'],
        inactive_bg=curcolors['0'],
        active_fg=curcolors['bg'],
        active_bg=curcolors['2'],
        font="JetBrainsMono Nerd Font Mono",
        fontsize=18,
        padding=6,
        section_fontsize=14,
        section_padding=4,
        section_fg=curcolors['fg']
    ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
