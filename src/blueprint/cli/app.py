from arc import CLI

cli = CLI()


@cli.command()
def command():
    print("Hello there!")
