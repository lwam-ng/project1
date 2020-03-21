# First, get the template files
top_template = open('./template/top.html').read()
bottom_template = open('./template/bottom.html').read()

# Read in content HTML files
index = open('./content/index.html').read()
about = open('./content/about.html').read()
services = open('./content/services.html').read()

# Combine template HTML code with content HTML code
open('./docs/index.html', 'w+').write(top_template + index + bottom_template)
open('./docs/about.html', 'w+').write(top_template + about + bottom_template)
open('./docs/services.html', 'w+').write(top_template + services + bottom_template)