import logging
import os

import gitlab

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

URL = os.environ['CI_SERVER_URL']
TOKEN = os.environ['GITLAB_TOKEN']

gl = gitlab.Gitlab(URL, private_token=TOKEN, ssl_verify=True)

for runner in runners:
    try:
        if runner.status != "online":
            LOG.info(f'Deleting {runner.id}::{runner.description}')
            runner.delete()

    except Exception as ex:
        LOG.exception(ex)
