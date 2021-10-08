import cgi
import os
import http.cookies


cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
count = cookie.get("count")
if count is None:
    print("Set-cookie: count=1")
else:
    c = int(count.value) + 1
    print(f"Set-cookie: count={c}")




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
print(cookie.get("count"))
print("<hr>")
for k, v in os.environ.items():
    print(f"<p>Key = {k} value = {v}</p>")

print("""</body>
        </html>""")

