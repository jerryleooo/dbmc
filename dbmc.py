# -*- coding: utf-8 -*-

import os
import sys
import codecs
import requests
from jinja2 import Environment, PackageLoader
import config

def generate_md(dbid):
    _url = 'https://api.douban.com/v2/book/user/%s/collections'
    r = requests.get(_url % dbid)
    books = r.json()['collections']

    readings = []
    reads = []
    wishes = []

    for item in books:
        if item['status'] == 'reading':
            readings.append(item)
        elif item['status'] == 'read':
            reads.append(item)
        elif item['status'] == 'wish':
            wishes.append(item)

    env = Environment(loader=PackageLoader('dbmc', config.TEMPLATE_DIR))
    template = env.get_template(config.TEMPLATE_FILE)
    output = "/".join([config.OUTPUT_DIR, config.OUTPUT_FILE])
    if not os.path.isdir(config.OUTPUT_DIR):
        os.mkdir(config.OUTPUT_DIR)
    with codecs.open(output, 'wb', 'utf-8') as fp:
        fp.write(template.render(readings=readings,
                                 reads=reads,
                                 wishes=wishes))

if __name__ == '__main__':
    dbid = config.DBID # My Douban id
    generate_md(dbid)
