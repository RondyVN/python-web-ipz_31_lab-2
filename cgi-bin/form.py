import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")

checkbox = form.getlist('lessons')
language = form.getlist('language')

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Info!</h1>")
print("<p>User text: {}</p>".format(text1))
print("<p>User text: {}</p>".format(text2))
print("<p>Lessons: {}".format(', '.join(checkbox)))
print("<p>language: {}".format(', '.join(language)))
print("""</body>
        </html>""")