# MIA-utils: utilities for maintenance of MIA

## building-trigger

A script to request all buildings together with their image URLs from the MIA API. 
This helps us (until we come up with a better solution ;)) to pre-generate thumbnails on the image server which otherwise would be created during the first display of the building in the apps and could cause a timeout error.

### Usage

Setup a virtual env and install requirements

```bash
$ python -m venv env
$ source env/bin/activate
$(env) cd building-trigger/
$(env) pip install -r requirements.txt
```

You will need to use an API token stored in a `token.txt` file.
```bash
$(env) cd building-trigger/
$(env) echo 'Your API token' > token.txt
```

Call the script with the number of buildings whose images you wish to pre-generate.
```bash
$(env) python trigger.py 10
```
