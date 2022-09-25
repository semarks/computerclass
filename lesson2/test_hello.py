#!/usr/bin/env python3

"""Pytest file to test hello.py.

"""

import hello

def test_hello_world() -> None:
    """Test hello_world

    Parameters
    ----------
    [None]

    Returns
    ----------
    None
    """

    hello_str = hello.hello_world()

    assert hello_str == "Hello World"


def test_goodbye() -> None:
    """Test goodbye

    Parameters
    ----------
    [None]

    Returns
    ----------
    None
    """

    goodbye_str = hello.goodbye()

    assert goodbye_str == "Goodbye!"


