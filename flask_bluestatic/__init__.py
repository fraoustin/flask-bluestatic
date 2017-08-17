#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Module flask_bluestatic
"""

__version_info__ = (0, 1, 0)
__version__ = '.'.join([str(val) for val in __version_info__])

__namepkg__ = "flask-bluestatic"
__desc__ = "Flask BlueStatic module"
__urlpkg__ = "https://github.com/fraoustin/flask-bluestatic.git"
__entry_points__ = {}

from .main import BlueStatic
