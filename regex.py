#!/usr/bin/env python3

import re

TAGS = re.compile(r'\[(.*?)\]')

TITLE = re.compile(r'\s([^][]*)$')

TAG_REFERENCE = re.compile(r'''[^\\] #we look for an unescaped %
        (%
        (?:\[\d*\])? #there may be several tags
        (?:\[\d*\])? #there may be words specified
        )''',
        re.X)

TITLE_REFERENCE = re.compile(r'''[^\\] #we look for an unescaped #
        (\#
        (?:\[\d*\])? # there may be words specified
        )''',
        re.X)

