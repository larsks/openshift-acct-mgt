import json
import logging

LOG = logging.getLogger(__name__)


def exists_openshift_user(api, user_name):
    url = f'/apis/user.openshift.io/v1/users/{user_name}'
    r = api.get(url)

    LOG.warning("url: " + url)
    LOG.warning("exists os user: " + str(r.status_code))
    LOG.warning("exists os user: " + r.text)
    return r.status_code == 200 or r.status_code == 201


def create_openshift_user(api, user_name, full_name):
    url = '/apis/user.openshift.io/v1/users'
    payload = {
        "kind": "User",
        "apiVersion": "v1",
        "metadata": {"name": user_name},
        "fullName": full_name,
    }
    r = api.post(url, data=json.dumps(payload))

    LOG.debug("url: " + url)
    LOG.debug("payload: " + json.dumps(payload))
    LOG.debug("r: " + str(r.status_code))
    LOG.debug("r: " + r.text)
    return r


def delete_openshift_user(api, user_name):
    url = f'/apis/user.openshift.io/v1/users/{user_name}'
    r = api.delete(url)
    LOG.debug("url: " + url)
    LOG.debug("d os user: " + str(r.status_code))
    LOG.debug("d os user: " + r.text)
    return r
