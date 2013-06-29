#!/usr/bin/env python3

import sys

import regex
import parser

def main(email):
    for line in email.splitlines():
        if line.startswith('Subject:'):
            subject = line
            break
    
    text = email

    tags = parser.parse_tags(subject)
    title = parser.parse_title(subject)

    tag_references = regex.TAG_REFERENCE.findall(text)
    title_references = regex.TITLE_REFERENCE.findall(text)

    try:
        for tag_reference in tag_references:
            text = parser.replace_tag_reference(text, tags, tag_reference)

        for title_reference in title_references:
            text = parser.replace_title_reference(text, title, title_reference)
    except (IndexError, TypeError, AttributeError):
        return email

    print(text)
    return text

if __name__ == '__main__':
    email_file = open(sys.argv[1], 'r')
    email = email_file.read()
    email_file.close()

    main(email)

