import glob
import os
from jinja2 import Template

def glob_content():
    all_html_files = glob.glob("./content/*.html")
    return all_html_files

def generate_pages_list():
    pages_list = []
    all_html_files = glob_content()
    for html_file in all_html_files:
        file_path = html_file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        pages_list.append({
            "filename": file_path,
            "title": name_only.capitalize(),
            "output_filename": file_name,
            "output_filepath": "docs/" + file_name
        })
    return pages_list

def render_pages():
    pages = generate_pages_list()
    for page in pages:
        html_page = open(page['filename']).read()
        template_html = open("./template/base.html").read()
        template = Template(template_html)
        final_page = template.render(
            title=page['title'],
            content=html_page,
            pages=pages
        )
        open(page['output_filepath'], "w+").write(final_page)


def new_content():
    new_html = "<h1>New Content!</h1>\n\n<p>New content...</p>"
    open('./content/new_content_page.html', "w+").write(new_html)
