# {{cookiecutter.project_name}}
{{cookiecutter.short_description}}

![featured_image](images/mhk_logotype.png)

## Liens
 * [documentation du projet]({{cookiecutter.docs_url}})
 * [page d'accueil du projet sur le GesLab]({{cookiecutter.geslab_url}})
 * [page wiki du projet sur le wiki du Humanlab]({{cookiecutter.wikilab_url}})
 * [canal de discussion sur Framateam]({{cookiecutter.framateam_url}})

## Fonctionnalités
Ce dépôt GitHub est principalement utilisé pour stocker l'ensemble des informations (documents, modèles 3D, code, plans, etc.) nécessaires au projet _{{cookiecutter.project_name}}_.

Le fichier _project.json_ permet notamment de générer la documentation finale du projet à l'aide de l'outil [myworkshop](https://github.com/myhumankit/myworkshop).

## Installation
[Téléchargez ce dépôt](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}}/archive/master.zip) et décompressez le dans le répertoire de votre choix. Renommez le dossier `{{cookiecutter.generic_name}}-master` en `{{cookiecutter.generic_name}}`.

Il est possible de cloner directement ce dépôt dans le répertoire de votre choix :

```
$ git clone git@github.com:{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}}.git
```

## Briques technologiques utilisées
 * [myworkshop](https://github.com/myhumankit/myworkshop).

## Gestion de version
La gestion de version repose sur le système [SemVer](http://semver.org/). Voir le fichier [CHANGELOG.md](CHANGELOG.md) pour plus de détails.

## Contribuer
Si vous souhaitez contribuer au projet, merci de créer une _issue_ ou de _forker_ ce projet et de créer une nouvelle branche. Toutes les _pull requests_ sont les bienvenues !

## Licence
Ce projet est diffusé sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de details.

## Contributeurs
 * **{{cookiecutter.full_name}}** - [{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}})

---

# {{cookiecutter.project_name}}

## Links
 * [Documentation page of the project]({{cookiecutter.docs_url}})
 * [Home page of the project on GesLab]({{cookiecutter.geslab_url}})
 * [Page of the project on the wiki of the Humanlab]({{cookiecutter.wikilab_url}})
 * [Framateam collaboration channel]({{cookiecutter.framateam_url}})

## Features
This very GitHub repository is used to collect all available information (documents, 3D models, code, blueprints, etc.) regarding the project _{{cookiecutter.project_name}}_.

The _project.json_ file allows the final documentation generation using the tool [myworkshop](https://github.com/myhumankit/myworkshop).

## Installation
[Download this repository](https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}}/archive/master.zip) and unzip it into the Arduino libraries folder on your computer. You should rename the folder `{{cookiecutter.generic_name}}-master` in `{{cookiecutter.generic_name}}`.

Or clone the repository directly in the Arduino libraries folder:

```
git clone git@github.com:{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}}.git
```

## Technologie used
 * [myworkshop](https://github.com/myhumankit/myworkshop).

## Versioning
We use [SemVer](http://semver.org/) for versioning. See the [CHANGELOG.md](CHANGELOG.md) file for details.

## Contributing
If you'd like to contribute, please raise an issue or fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contributors
 * **{{cookiecutter.full_name}}** - [{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}})
