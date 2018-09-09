import sys
from ruamel.yaml import YAML

input_readme = open("README.yaml").read()

yaml = YAML()

yaml.dump(yaml.load(input_readme), sys.stdout)
