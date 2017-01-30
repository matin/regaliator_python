from regalii.clients import v31


class Configuration(object):
    def __init__(self, api_key, secret_key, host,
                 timeout=60,
                 use_ssl=True,
                 proxy_host=None, proxy_port=None, proxy_user=None, proxy_pass=None,
                 version=v31.API_VERSION):
        self.api_key = api_key
        self.secret_key = secret_key
        self.host = host
        self.timeout = timeout
        self.use_ssl = use_ssl
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_user = proxy_user
        self.proxy_pass = proxy_pass
        self.version = version

    def secure(self):
        return self.use_ssl
