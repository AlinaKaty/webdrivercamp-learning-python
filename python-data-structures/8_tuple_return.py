#!/usr/bin/python3
def tuple_return(arg):
    if not arg:
        return (None, None)
    return (len(arg), arg[0])
