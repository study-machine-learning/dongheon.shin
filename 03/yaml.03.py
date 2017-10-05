import yaml

content = """
color_def:
    - &color1 "#FF0000"
    - &color2 "#00FF00"
    - &color3 "#0000FF"
color:
    title: *color1
    body: *color2
    link: *color3
"""

data = yaml.load(content)

print("title = ", data["color"]["title"])
print("body = ", data["color"]["body"])
print("link = ", data["color"]["link"])
