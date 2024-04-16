"Tools and utilities related to functional programming."


def identity(a, *args):
    "Return the same thing back."
    return (a, *args) if args else a
