import json
import requests
import subprocess


# est-ce que le projet existe sur le wikilab ?
# si non :
#     -> message : "INFO : creation of a new page on wikilab"
#     -> créer une nouvelle page sur wikilab
r = requests.get('{{cookiecutter.wikilab_url|e}}')
if r.status_code == 200:
    print('INFO: this project already exists on WikiLab.')
else:
    print('INFO: project not found on WikiLab.')
    S = requests.Session()
    URL = "http://wikilab.myhumankit.org/api.php"
    text = '''== Description du projet ==
{{ cookiecutter.short_description|e }}

== Liens utiles ==
* [{{cookiecutter.geslab_url|e}} Page du projet sur le GesLab]
* [{{cookiecutter.framateam_url|e}} Canal de discussion du projet sur Framateam]
* [{{cookiecutter.docs_url|e}} Documentation finale du projet]
* [https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}} Dépôt GitHub du projet]

== Cahier des charges ==

== Analyse de l'existant ==

== Equipe (Porteur de projet et contributeurs) ==
* Porteur de projet
* Contributeurs
* Animateur (coordinateur du projet)
* Fabmanager référent
** {{cookiecutter.full_name|e}}
* Responsable de documentation

== Matériel nécessaire ==

== Outils nécessaires ==

== Coût ==

== Délai estimé ==

== Fichiers source ==

== Étapes de fabrication pas à pas ==

== Durée de fabrication du prototype final ==


[[Category:Projets]]'''

    # Step 1: Retrieve a login token
    PARAMS_1 = {
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_1)
    if not R.ok:
        print('ERROR: error retrieving a login token on wikilab!')
    else:
        print('INFO: retrieve a login token successfully on wikilab.')
        DATA = R.json()
        LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

        # Step 2: Send a post request to log in.
        PARAMS_2 = {
            "action": "login",
            "lgname": "{{cookiecutter.wikilab_username}}",
            "lgpassword": "{{cookiecutter.wikilab_password}}",
            "format": "json",
            "lgtoken": LOGIN_TOKEN
        }

        R = S.post(URL, data=PARAMS_2)
        if not R.ok:
            print('ERROR: error login on wikilab!')
        else:
            print('INFO: successfull login on wikilab.')

            # Step 3: While logged in, retrieve a CSRF token
            PARAMS_3 = {
                "action": "query",
                "meta": "tokens",
                "format": "json"
            }

            R = S.get(url=URL, params=PARAMS_3)
            if not R.ok:
                print('ERROR: error retrieving a CSRF token on wikilab!')
            else:
                print('INFO: retrieve a CSRF token successfully on wikilab.')
                DATA = R.json()
                CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

                # Step 4: Send a post request to edit a page
                PARAMS_4 = {
                    "action": "edit",
                    "title": "Projets:{{cookiecutter.wikilab_name|e}}",
                    "format": "json",
                    "text": text,
                    "token": CSRF_TOKEN
                }

                R = S.post(URL, data=PARAMS_4)
                if R.ok:
                    print('INFO: wikilab page successfully created.')
                else:
                    print('ERROR: error creating wikilab page!')


# on crée le dépôt GitHub
# on s'assure que le json est valide
data = json.loads('{"name":"{{cookiecutter.generic_name}}","description":"{{cookiecutter.short_description|e}}","homepage":"{{cookiecutter.docs_url|e}}"}')
data = json.dumps(data)
r = requests.post('https://api.github.com/orgs/{{cookiecutter.github_organization}}/repos',
                  data = data,
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
print('################################################################################')
print('# Ajouter manuellement les liens suivants dans la page du projet sur le GesLab #')
print('################################################################################')
print('Intitulé : Page du projet sur wikilab')
print('URL      : {{cookiecutter.wikilab_url|e}}')
print('--------------------------------------------------------------------------------')
print('Intitulé : Canal de discussion du projet sur Framateam')
print('URL      : {{cookiecutter.framateam_url|e}}')
print('--------------------------------------------------------------------------------')
print('Intitulé : Documentation du projet')
print('URL      : {{cookiecutter.docs_url|e}}')
print('--------------------------------------------------------------------------------')
print('Intitulé : Dépôt GitHub du projet')
print('URL      : https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.generic_name}}')
print('################################################################################')
print('# Créer un nouveau canal sur l\'équipe My Human Kit de Framateam                #')
print('################################################################################')
print('Nom         : {{cookiecutter.generic_name}}')
print('Description : {{cookiecutter.short_description|e}}')
print('Entête      : [{{cookiecutter.project_name|e}}](https://dev.humanlab.me/projet/{{cookiecutter.generic_name}}/)')
print('--------------------------------------------------------------------------------')
