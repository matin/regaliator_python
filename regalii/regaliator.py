from regalii.clients import v15
from regalii.clients import v30
from regalii.clients import v31
from regalii.exceptions import APIVersionError


class Regaliator(object):
    API_VERSIONS = {
        v15.API_VERSION: v15.Client,
        v30.API_VERSION: v30.Client,
        v31.API_VERSION: v31.Client,
    }

    def __init__(self, configuration):
        if configuration.version not in Regaliator.API_VERSIONS.keys():
            raise APIVersionError(configuration.version)

        self.client = Regaliator.API_VERSIONS[configuration.version](configuration)
        self.account = self.client.account
        self.bill = self.client.bill
        self.biller = self.client.biller
        self.rate = self.client.rate
        self.transaction = self.client.transaction
