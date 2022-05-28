import re
from lib import texttohtml

TEMPLATE = ["home.html", "whoami.html", "resume.html", "bin.html", "article.html", "404.html"]
COMMON = "common.html"

if __name__ == "__main__":

    texttohtml.reset(files=TEMPLATE)

    html = open("templates/common.html", "r+")
    data = html.read()
    html.close()
    find = re.search("<pre><\/pre>", data)
    span = find.span()
    with open("static/textfile/common.txt", "r") as file:
        _data = file.read()
        data = data[:span[0]] + f"<pre>{texttohtml.texttohtml(_data)}</pre>" + data[span[1]:]
        with open("templates/common.html", "w") as f:
            f.write(data)
    for i in TEMPLATE:
        _path_text = "static/textfile/" + i[:-5] + ".txt"
        _path_html = "templates/" + i
        with open(_path_html, 'r+') as f:
            contents = f.read()
            with open(_path_text, 'r') as file:
                contents = contents[:48] + texttohtml.texttohtml(file.read()) + contents[48:]
                f.seek(0)
                f.truncate()
                f.write(contents)