import json
import re

from app import app


def cnvt_project_name(project_name):
    suggested_project_name = re.sub("^[^A-Za-z0-9]+", "", project_name)
    suggested_project_name = re.sub("[^A-Za-z0-9]+$", "", suggested_project_name)
    suggested_project_name = re.sub("[^A-Za-z0-9-]+", "-", suggested_project_name)
    return suggested_project_name


def exists_openshift_project(api, project_name):
    url = f'/apis/project.openshift.io/v1/projects/{project_name}'
    r = api.get(url)
    app.logger.debug("url: " + url)
    app.logger.debug("r: " + str(r.status_code))
    app.logger.debug("r: " + r.text)
    if r.status_code == 200 or r.status_code == 201:
        return True
    return False


def delete_openshift_project(api, project_name):
    url = f'/apis/project.openshift.io/v1/projects/{project_name}'
    r = api.delete(url)
    app.logger.debug("url: " + url)
    app.logger.debug("r: " + str(r.status_code))
    app.logger.debug("r: " + r.text)
    return r


def create_openshift_project(api, project_uuid, project_name, user_name):
    url = '/apis/project.openshift.io/v1/projects'

    payload = {
        "kind": "Project",
        "apiVersion": "project.openshift.io/v1",
        "metadata": {
            "name": project_uuid,
            "annotations": {
                "openshift.io/display-name": project_name,
                "openshift.io/requester": user_name,
            },
        },
    }
    r = api.post(url, data=json.dumps(payload))
    app.logger.debug("url: " + url)
    app.logger.debug("payload: " + json.dumps(payload))
    app.logger.debug("r: " + str(r.status_code))
    app.logger.debug("r: " + r.text)
    return r
