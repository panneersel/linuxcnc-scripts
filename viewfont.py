#!/usr/bin/env python
import sys
from fontTools.ttLib import TTFont

with TTFont(sys.argv[1], 0, ignoreDecompileErrors=True) as ttf:
    for x in ttf["cmap"].tables:
        for (_, code) in x.cmap.items():
            point = code.replace('uni', '\\u').lower()
            print("echo -e '" + point + "'")
