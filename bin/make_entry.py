#!/usr/bin/env python
import sys
from datetime import date

TEMPLATE = """
title: {title}
date: {year}-{month}-{day}
tags:
category: {category}
slug: {slug}
{{% from 'fancybox.html' import fancybox %}}

<!-- PELICAN_END_SUMMARY -->
"""


def make_entry(category,title):
    today = date.today()
    slug = title.lower().strip().replace(' ', '_')
    f_create = "content/{}/{}-{:0>2}-{:0>2}-{}.md".format(category,
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=format(today.month, '02'),
                                day=format(today.day, '02'),
                                category=category,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 2:
        make_entry(sys.argv[1],sys.argv[2])
    else:
        print("No title or category given eg ./{} 'category' 'title'".format(sys.argv[0]))
