from yaml import load, Loader
import re
import sys

class Yaml2ProbaTree:
    def __init__(self, debug=False):
        self.debug = debug

    def indent(self, text):
        text = "\t"+text
        return text.replace("\n", "\n\t")

    def parse_weight(self, weight):
        p = re.compile('([0-9]*)\/([0-9]*)')
        return p.sub(r'$\\frac{\1}{\2}$', weight)

    def recurse_node(self, node, name, n=0):
        if not node:
            print(f"[log] node `{name}` is corrupted")
            return
        if not "_v" in node.keys():
            weight = None
        else:
            weight = self.parse_weight(node["_v"])
        last = len(node.keys()) == 1
        text = ""
        if n > 0:
            if last:
                text =  """node[end, label=right:\n"""
                text += """\t{"""+name+"""}] {}\n"""
            else:
                text =  """node[mytree] {"""+name+"""}\n"""
        texts = [self.recurse_node(child_node, child_name, n=n+1)
            for child_name, child_node in node.items()
            if child_name != "_v"]
        text += '\n'.join(list(map(lambda t: """child {\n"""+self.indent(t)+"""\n}""", reversed(texts))))+'\n'

        if n > 0:
            text = text.strip()
            text += """\nedge from parent\n"""
            text += """node[above]  {"""+weight+"""}"""
        if name == "Root":
            text = """\\node[mytree] {}\n\t""" + self.indent(text).strip()+ """;\n"""
        return text

    def yaml2tikz(self, input_yaml_file=None):
        if input_yaml_file == None:
            text = ''.join([ line for line in sys.stdin])
            # Yaml doesn't work with tabs
            text = text.replace('\t', '  ')
            if self.debug:
                print(f"[log] stdin : `{text}`")
            data = load(text, Loader=Loader)
        else:
            with open(input_yaml_file, "r") as input_tree:
                # Yaml doesn't work with tabs
                input_tree = input_tree.replace('\t', '  ')
                data = load(input_tree, Loader=Loader)
        if not "root" in data.keys():
            print("[error] No root node, exiting...")
            exit(1)
        result = """
% Set the overall layout of the tree
\\tikzstyle{level 1}=[level distance=3.5cm, sibling distance=3.5cm]
\\tikzstyle{level 2}=[level distance=3.5cm, sibling distance=2cm]
% Define styles for mytree and leafs
\\tikzstyle{mytree} = [text width=4em, text centered]
\\tikzstyle{end} = [circle, minimum width=3pt,fill, inner sep=0pt]

\\begin{tikzpicture}[grow=right, sloped]
    """
        result += self.recurse_node(data["root"], "Root")
        result += """\end{tikzpicture}"""
        return result


