pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },

    {
        "filename": "content/services.html",
        "output": "docs/services.html",
        "title": "Services",
    },

    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Us",
    }
]


def main():
    base = open('./template/base.html').read()
    for page in pages:
        final_page = combine(page, base)
        open(page['output'], "w+").write(final_page)


def combine(page, base):
    print_logs(page)
    content = open(page['filename']).read()
    final = base.replace("{{content}}", content)
    final = final.replace("{{Title}}", page['title'])
    return final


def print_logs(page):
    print("This is: ", page['title'])
    print("File name: ", page['filename'])
    print("Can be found in: ", page['output'])


main()
