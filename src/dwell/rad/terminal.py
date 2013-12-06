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


try:
    from argh import ArghParser
    import log as mylog
    import sys
    def argh_main(progname, commands):
        parser = ArghParser()
        parser = ArghParser()
        parser.add_argument("--very_verbose", action="store_true")
        mylog.command_line(parser, progname, default_verbosity="CRITICAL", default_file_verbosity="INFO")

        parser.add_commands(commands)
        args = parser.parse_args()
    
        log = mylog.default_logger(progname,
                                    logfile=args.logfile,
                                    verbosity=args.verbosity, 
                                    file_verbosity=args.file_verbosity)
    
        try:
            parser.dispatch()
        except KeyboardInterrupt as e:
            log.info("Exiting on Keyboard Interrupt")
            print("Exiting on Keyboard Interrupt")
        except Exception, e:
            print ("ERROR: {0}".format(e))
            log.error(e.message)
            if args.very_verbose:
                raise
            else:
                sys.exit(1)
except:
    def argh_main(progname, commands):
        print ("Import of argh module failed")
        import sys
        sys.exit(1)