import re

def parse_markdown(markdown):
    lines = markdown.split('\n')
    response, in_list = '', False
    for line in lines:
        line = markdown_emphasis(line)
        line, in_list = markdown_list(line, in_list)
        if not in_list:
            line = markdown_titles(line)
            line = markdown_paragraph(line)
        response += line
    if in_list:
        response += '</ul>'
    return response


def markdown_emphasis(line):
    #bold
    for found in re.findall(r'\b__.*__\b', line):
        line = line.replace(found, f'<strong>{found[2:-2]}</strong>')

    #italic
    for found in re.findall(r'\s_.*_\s', line):
        line = line.replace(found, f' <em>{found[2:-2]}</em> ')

    return line

def markdown_titles(line):
    hashtags = re.match(r'^[#]+\s', line)
    if hashtags:
        number = hashtags.group().count('#')
        line = f'<h{number}>' + line[number + 1:] + f'</h{number}>'
    return line

def markdown_list(line, in_list):
    if re.match(r'^\*\s', line):
        line = '<li>' + line[2:] + '</li>'
        if not in_list:
            line = '<ul>' + line
            in_list = True
    else:
        if in_list:
            in_list = False
            line += '</ul>'
    return line, in_list

def markdown_paragraph(line):
    if not re.match('<h|<ul|<p|<li', line):
        line = f'<p>{line}</p>'
    return line