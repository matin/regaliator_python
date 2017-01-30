

class APIVersionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "API version '{api_version}' isn't supported!".format(api_version=self.message)
