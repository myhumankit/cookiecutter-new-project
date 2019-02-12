import re
import sys
import requests

# est-ce que le generic_name a un format adéquate ?
# des minuscules seulement
# des tirets (-)
# pas d'espace
# pas de nombre
GENERIC_NAME_REGEX = r'^[a-z][-a-z]+[a-z]$'
generic_name = '{{ cookiecutter.generic_name }}'
if not re.match(GENERIC_NAME_REGEX, generic_name):
    print('ERROR: %s is not a valid generic name!' % generic_name)
    sys.exit(1) # exits with status 1 to indicate failure
else:
    print('INFO: %s is a valid generic name.' % generic_name)


# est-ce que le projet existe sur le GesLab ?
# si non :
#     -> message : "ERROR: please create this project on GesLab first!"
#     -> abort
geslab_url = '{{ cookiecutter.geslab_url|e }}'
r = requests.get(geslab_url)
print(r.status_code)
if not r.status_code == 200:
    print('ERROR: please create this project on GesLab first!')
    sys.exit(1) # exits with status 1 to indicate failure
else:
    print('INFO: GesLab project found.')


# est-ce que le projet exite sur GitHub ?
# si oui :
#     -> message : "ERROR: this GitHub repository already exists!"
#     -> abort
github_url = 'https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.generic_name }}'
r = requests.get(github_url)
print(r.status_code)
if r.status_code == 200:
    print('ERROR: this GitHub repository already exists!')
    sys.exit(1) # exits with status 1 to indicate failure
else:
    print('INFO: GitHub name for this repository is availlable.')
