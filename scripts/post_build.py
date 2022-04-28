import os

to_find = 'Published with <a href="https://wowchemy.com/?utm_campaign=poweredby" target=_blank rel=noopener>Wowchemy</a> — the free, <a href=https://github.com/wowchemy/wowchemy-hugo-modules target=_blank rel=noopener>open source</a> website builder that empowers creators.'

for direc_name, dirs, files in os.walk("../public"):
    for file_name in files:
        path = os.path.join(direc_name, file_name)
        if(path[-5:] == ".html"):
            data = open(path, "r").read()
            data = data.replace("\n", "")
            data = data.replace(to_find, "")
            open(path, "w").write(data)
