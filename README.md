# cookiecutter-new-project
[Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a new MHK project.

## Features
 * Run usefull commands to generate all the tool stack for a new MHK project (GesLab, wikilab, Framateam, etc.);
 * Initialize a Git ripository with all the requirements for a new documentation project with [myworkshop](https://github.com/myhumankit/myworkshop).

## Getting started

### Requirements
 * git 2.17.1 or higher (package _git_);
 * python 3.6.7 or higher (package _python3_);
 * pip 19.0.1 or higher (package _python3-pip_);
 * coockiecutter 1.6.0 or higher;
 * requests 2.18.4 or higher.

Install the latest Cookiecutter (if you haven't installed it yet!) and _requests_ :

```
sudo pip3 install cookiecutter
sudo pip3 install requests
```

### Configuration
By default Cookiecutter tries to retrieve settings from a _.cookiecutterrc_ file in your home directory. Please create this file with some default settings :

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
Generate a new project:

```
cookiecutter https://github.com/myhumankit/cookiecutter-new-project.git
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
