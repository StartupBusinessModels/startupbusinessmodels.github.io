'''
../StartupAtlas/raw_markdowns/cleverism_raw/
'''

import glob

layout = \
'''---
layout: post
title: %s
---

%s
'''


files = glob.glob("../StartupAtlas/raw_markdowns/cleverism_raw/*")
for file in files:
	title = file.rsplit("/")[-1].replace(".md", "")

	f = open(file, 'r')
	content = f.read()
	content = "\n".join(["".join(line.split(" ", 1)) for line in content.split("\n")])
	f.close()

	g = open("_posts/2017-10-25-%s.md" % title, "wb")
	g.write(layout % (title, content))
	g.close()

	# break

