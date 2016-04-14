#!/usr/bin/env python

from os.path import abspath, join, basename, dirname, isdir
from os import listdir


docsdir = abspath(join(dirname(abspath(__file__)), '..','docs'))
tpl = join(docsdir, '_header.md')
out = join(docsdir, 'index.md')
with open(out, 'wt') as index:
    index.write(open(tpl, 'rt').read())
    for dir in listdir(docsdir):
        fulldir = join(docsdir, dir)
        if not isdir(fulldir):
            continue
        subs = [d for d in listdir(fulldir) if isdir(join(fulldir, d))]
        index.write('- {}\n'.format(dir))
        for sub in subs:
            index.write('{ws}- {sub} [main]({dir}/{sub}/index.html) | [class index]({dir}/{sub}/classes.html)\n'.format(ws=' '*4, sub=sub, dir=dir))
            print('{ws}- {sub} [main]({dir}/{sub}/index.html) | [class index]({dir}/{sub}/classes.html)\n'.format(ws=' '*4, sub=sub, dir=dir))

