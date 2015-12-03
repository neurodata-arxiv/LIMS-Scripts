import ndio.remote.OCPMeta as LIMS
import json

lims = LIMS()

secret = "neurodata"
filename = 'w.ocp.me.images.json'

with open(filename) as data_file:
    data = json.load(data_file)


for project in data:
    project['secret'] = secret
    lims.set_metadata(project['token'], project)
