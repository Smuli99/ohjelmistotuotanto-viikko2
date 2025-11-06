from project_reader import ProjectReader


def main():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/test-project/pyproject.toml"
    project = ProjectReader(url).get_project()
    print(project)


if __name__ == "__main__":
    main()
