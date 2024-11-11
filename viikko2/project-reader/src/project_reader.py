import tomllib
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content)
        
        # TODO: Check if exists
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        license = data["tool"]["poetry"]["license"]
        authors = data["tool"]["poetry"]["authors"]
        dependencies = data["tool"]["poetry"]["dependencies"].keys()
        dev_dependencies = data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()

        return Project(name, description, license, authors, dependencies, dev_dependencies)
