#!/usr/bin/env python3

import re
import regex

def parse_tags(subject):
    tags = regex.TAGS.findall(subject)

    new_tags = []
    for tag in tags:
        new_tags.append(re.split(r'\s|[\'-]', tag))

    tags = list(new_tags)
    del new_tags

    return tags

def parse_title(subject):
    title = regex.TITLE.findall(subject)

    assert(len(title) == 1)
    
    title = title[0]
    title = re.split(r'\s|[\'-]', title)

    return title

def replace_tag_reference(text, tags, tag_reference):
    match = re.findall(r'(\d)+', tag_reference)

    if match == []:
        tag_reference = r'([^\\]){0}'.format(tag_reference)
        word = r'\1{0}'.format(' '.join(tags[0]))
    else:
        tag_reference = re.escape(tag_reference)
        if len(match) == 1:
            if len(tags) == 1:
                word = tags[0][int(match[0])]
            else:
                word = ' '.join(tags[int(match[0])])
        else:
            word = tags[int(match[0])][int(match[1])]

    return re.sub(tag_reference, word, text)

def replace_title_reference(text, title, title_reference):
    match = re.findall(r'(\d)+', title_reference)

    if match == []:
        title_reference = r'([^\\]){0}'.format(title_reference)
        word = r'\1{0}'.format(' '.join(title))
    else:
        title_reference = re.escape(title_reference)
        word = title[int(match[0])]

    return re.sub(title_reference, word, text)

