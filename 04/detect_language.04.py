#!/usr/bin/env python3
from sklearn.externals import joblib

import cgi
import os.path

languages = {
    "en": "english",
    "fr": "french",
    "tl": "tagalog",
    "id": "bahasa indonesia"
}


def provide_form(text, message=""):

    print("Content-Type: text/html; charset=utf-8\n")
    print("")
    print("""
        <html>
            <body>
                <form>
                    <textarea name="text" rows="8" cols="40">{0}</textarea>
                    <p><input type="submit" value="detect"></p>
                    <p>{1}</p>
                </form>
            </body>
        </html>
    """.format(cgi.escape(text), message))


def detect_language(text):

    text = text.lower()

    count = [0 for i in range(0, 26)]

    for ch in text:

        n = ord(ch) - ord("a")

        if 0 <= n < 26:
            count[n] += 1

    total = sum(count)

    if total is 0:
        return "no input"

    frequencies = list(map(lambda n: n / total, count))

    res = classifier.predict([frequencies])
    return languages[res[0]]


filename = os.path.dirname(__file__) + "/frequencies.pkl"
classifier = joblib.load(filename)

form = cgi.FieldStorage()

text = form.getvalue("text", default="")
message = ""

if text != "":

    language = detect_language(text)
    message = "result = " + language

# requisites : sklearn, numpy, scipy
# PYTHONIOENCODING=utf-8:surrogateescape python3 -m http.server --cgi 8000
provide_form(text, message)
