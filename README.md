# cookiecutter-new-project
[Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a new MHK project.

## Features
 * Test if the new project already exists on GesLab (required), GitHub (forbiden) and wikilab (optionnal);
 * Initialize a Git ripository with all the requirements for a new documentation project with [myworkshop](https://github.com/myhumankit/myworkshop);
 * Create a new wikilab page if required.

## Getting started

### Requirements
Please install the latest [new-project Makefile](https://github.com/myhumankit/new-project) (if you haven't installed it yet!) :

```
$ cd ~/dev/
$ git clone git@github.com:myhumankit/new-project.git
$ cd new-project/
$ make install
```

### Configuration
By default, Cookiecutter tries to retrieve settings from a _.cookiecutterrc_ file in your home directory. Please create this file with some default settings :

```
default_context:
    full_name: ""
    email: ""
    github_username: ""
    github_token: ""
    wikilab_username: ""
    wikilab_password: ""
```

A _Personal access token_ is required to automatically create a new GitHub repository with this Cookiecutter template. Please generate a new token in _Settings/Developer settings/Personal access tokens_ with the _repo_ access (_Full control of private repositories_).

### Usage
Generate a new project with [new-project Makefile](https://github.com/myhumankit/new-project):

```
$ cd ~/dev/
$ make new
```

Or generate a new project directly with cookiecutter:

```
$ cookiecutter https://github.com/myhumankit/cookiecutter-new-project.git
```

## Tech/framework used
 * [cookiecutter](https://github.com/audreyr/cookiecutter).

## Versioning
We use [SemVer](http://semver.org/) for versioning. See the [CHANGELOG.md](CHANGELOG.md) file for details.

## Contributing
If you'd like to contribute, please raise an issue or fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contributors
 * **Julien Lebunetel** - [jlebunetel](https://github.com/jlebunetel)
