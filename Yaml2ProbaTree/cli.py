import click
import re
from Yaml2ProbaTree.yaml2probatree import Yaml2ProbaTree


def extract_part(content):
    p1 = re.compile('%% Tree Start.*')
    p2 = re.compile('%% Tree End.*')
    m1 = p1.search(content)
    m2 = p2.search(content)
    if not m1 or not m2:
        return []
    studied_part = content[m1.span()[0]:m2.span()[1]]
    if studied_part == []:
        return []
    next_part = extract_part(content[m2.span()[1]:])
    result = [studied_part]
    for i in next_part:
        result.append(i)
    return result

@click.command()
@click.option('-d', '--debug', is_flag=True)
@click.option('-l', '--refactor-latex', type=click.Path(), required=False)
@click.option('-y', '--input-yaml', type=click.Path(), required=False)
def cli(debug, refactor_latex=None, input_yaml=None):
    yaml2probatree = Yaml2ProbaTree(debug)
    if input_yaml:
        print(yaml2probatree.yaml2tikz(input_yaml_file=input_yaml))
    elif refactor_latex:
        with open(refactor_latex, "r") as refactor_latex_file:
            content = ''.join(refactor_latex_file.readlines())
            tabs = extract_part(content)
            for m in tabs:
                m = '\n'.join(m.split('\n')[1:][::-1][1:][::-1])
                replacement = yaml2probatree.yaml2tikz(yaml_text=m)+"\n"
                content = content.replace(m, replacement)
        print(content)
