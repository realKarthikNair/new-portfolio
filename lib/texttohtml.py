import re

with open("templates/template.html", "r") as f:
  COMMON_HTML = f.read()

def texttohtml(data:str) -> str:

    FLAG = 0
    MAP = []
    regex = [
        re.compile("\[[0-999]*\]"),
        re.compile("#!http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    ]

    for reg in regex:

        if FLAG == 0:
            _i = reg.findall(data)
            for i in range(len(_i)):
                find = reg.search(data)
                span = find.span()
                find = data[span[0]:span[1]]
                if find[1:-1] in MAP:
                  data = data[:span[0]] + f"[<a class='t' id='{find[1:-1]}' href='#{find[1:-1]}'>{find[1:-1]}</a>]" + data[span[1]:]
                else:
                  data = data[:span[0]] + f"[<a class='t' href='#{find[1:-1]}'>{find[1:-1]}</a>]" + data[span[1]:]
                MAP.append(find[1:-1])

        if FLAG == 1:
            _i = reg.findall(data)
            for i in range(len(_i)):
                find = reg.search(data)
                span = find.span()
                find = data[span[0]:span[1]]
                data = data[:span[0]] + f"<a href='{find[2:]}'>{find[2:]}</a>" + data[span[1]:]

        FLAG += 1

    return data

def reset(files:list, path="templates", common="common.html") -> None:

    with open(path+"/"+common, "w") as f:
        f.write(COMMON_HTML)

    for i in files:
        _path = path + "/" + i
        with open(_path, 'w') as file:
          print(_path)
          file.write("{% extends '" + common + "' %}\n{% block content %}\n\n{% endblock %}")
    return None

if __name__ == '__main__':
    with open("static/textfile/home.txt", "r") as file:
        with open("textfile.txt", "w") as out:
            data = texttohtml(file.read())
            out.write(str(data))