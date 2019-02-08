import requests
import subprocess


# est-ce que le projet existe sur le wikilab ?
# si non :
#     -> message : "INFO : creation of a new page on wikilab"
#     -> créer une nouvelle page sur wikilab
r = requests.get('{{cookiecutter.wikilab_url}}')
if r.status_code == 200:
    print('INFO: this project already exists on WikiLab.')
else:
    print('INFO: project not found on WikiLab.')
    # création à partir du template
    # --> to do


# on crée le dépôt GitHub
r = requests.post('https://api.github.com/orgs/{{cookiecutter.github_organization}}/repos',
                  data = '{"name":"{{cookiecutter.generic_name}}","description":"{{cookiecutter.short_description}}","homepage":"{{cookiecutter.docs_url}}"}',
                  headers={'Authorization': 'token {{cookiecutter.github_token}}'}
                 )
if r.status_code != 201: # on attend le code 201
    print('ERROR: unable to create a new GitHub repository!')
else:
    print('INFO: GitHub repository successfully created.')

    # on initialise le dépôt GitHub
    subprocess.call(['git', 'init'])
    # on commit
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', '"first commit"'])
    # on push
    subprocess.call(['git', 'remote', 'add', 'origin', 'git@github.com:{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}}.git'])
    subprocess.call(['git', 'push', '-u', 'origin', 'master'])

    # on ajoute le projet à la liste des projets sur myproject
    # --> to do


# on génère la fiche projet au format pdf ou svg
# --> to do


# on informe l'utilisateur :
#    -> ajout des liens du projet sur le GesLab
#    -> création manuelle du canal framateam
# --> to do
