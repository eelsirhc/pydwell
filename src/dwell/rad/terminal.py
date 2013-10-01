"""Terminal utilities"""

# termcolor
# if we have the termcolor package, then colorize some text.
try:
    from termcolor import cprint, colored
    def colorize(color, on_color=None):
        return lambda text: colored(text,color=color, on_color=on_color)

    message = colorize('blue')
    info    = colorize("green")
    warning = colorize('magenta')
    error = colorize('red')
    critical = colorize('red')
    note = colorize('grey')
except:

    def nocolor(text, *args, **kwargs):
        return text

    def colored(text, color=None, on_color=None, attrs=None):
        return text
    pass
    message = nocolor
    warning = nocolor
    error = nocolor
    critical = nocolor
    info = nocolor
    note = nocolor
