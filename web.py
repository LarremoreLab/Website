from collections import defaultdict
from webweb import Web
from pathlib import Path
import json
import yaml

DATA_PATH = Path.cwd().joinpath('_data')
PAPERS_PATH = DATA_PATH.joinpath('papers.yml')
PEOPLE_PATH = DATA_PATH.joinpath('people.yml')
SOFTWARE_PATH = DATA_PATH.joinpath('software.yml')
WEBWEB_JSON_PATH = DATA_PATH.joinpath('index_web.json')


def load_yaml(path):
    return yaml.load(path.read_text())


def clean_name(name):
    if name.endswith('*'):
        name = name[:-1]
    return name


def make_network(papers, people, software):
    nodes = defaultdict(dict)
    edges = []
    for paper in papers:
        title = paper['title']
        nodes[title] = {
            'name': title,
            'kind': 'paper'
        }

        for name in [clean_name(n) for n in paper['authors']]:
            nodes[name]['name'] = name
            nodes[name]['kind'] = 'collaborator'
            edges.append([title, name])

    for software_project in software:
        title = software_project['title']
        nodes[title] = {
            'name': title,
            'kind': 'software'
        }
        for name in [clean_name(n) for n in software_project['authors']]:
            nodes[name]['name'] = name
            nodes[name]['kind'] = 'collaborator'
            edges.append([title, name])

    dan = people['dan']
    for person in people['phd_students']:
        name = clean_name(person['name'])
        nodes[name]['name'] = name
        nodes[name]['kind'] = 'phd student'
        edges.append([dan['name'], name])

    for person in people['undergraduate_students']:
        name = clean_name(person['name'])
        nodes[name]['name'] = name
        nodes[name]['kind'] = 'undergraduate student'
        edges.append([dan['name'], name])

    nodes[dan['name']]['kind'] = 'dbl'
    web = Web(adjacency=edges, nodes=dict(nodes))
    web.display.colorBy = 'kind'
    web.display.colorPalette = 'Dark2'
    web.display.hideMenu = True
    web.display.showLegend = False

    WEBWEB_JSON_PATH.write_text(web.json)
    # web.show()


if __name__ == '__main__':
    papers = load_yaml(PAPERS_PATH)
    people = load_yaml(PEOPLE_PATH)
    software = load_yaml(SOFTWARE_PATH)

    make_network(papers, people, software)
