#!/usr/bin/env python3

"""Hello World Example.

This script is for educational purposes.  It will print
"Hello World" followed by "Goodbye!".

As a module, this file contains the following functions

* hello_world - returns the string "Hello World"
* goodbye - returns the string "Goodbye!"
"""

def hello_world() -> str:
    """'Hello World' string.

    Parameters
    ----------
    [None]

    Returns
    ----------
    str
        "Hello World"
    """

    hello_world_str = "Hello World"

    return hello_world_str


def goodbye() -> str:
    """'Goodbye!' string.

    Parameters
    ----------
    [None]

    Returns
    ----------
    str
        "Goodbye!"
    """

    goodbye_str = "Goodbye!"
    
    return goodbye_str



if __name__ == "__main__":

    hello_str = hello_world()
    goodbye_str = goodbye()

    print(hello_str)
    print(goodbye_str)


