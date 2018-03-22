import hmac
import json
import logging
import urllib

from base64 import b64encode
from datetime import datetime
from hashlib import sha1, md5

import pytz
import requests

from regalii import VERSION

logger = logging.getLogger('regaliator')


class EndPoint(object):
    def __init__(self, configuration):
        self.configuration = configuration

    def request(self, endpoint, params=None):
        return Request(self.configuration, endpoint, params)


class Response(object):
    PAGINATION_HEADER = 'X-Pagination'

    def __init__(self, response):
        self.response = response

    def data(self):
        result = None
        try:
            result = self.response.json()
            if self.paginated():
                result['pagination'] = self.pagination()
        except Exception:
            result = {
                'message': 'Server returned a non-json error'
            }

        return result

    def success(self):
        return self.response.status_code in (200, 201)

    def fail(self):
        return not self.success()

    def paginated(self):
        return Response.PAGINATION_HEADER in self.response.headers

    def pagination(self):
        return self.response.headers.get(Response.PAGINATION_HEADER)


class Request(object):
    CONTENT_TYPE = 'application/json'

    def __init__(self, config, endpoint, params=None):
        self.config = config
        self.endpoint = endpoint
        self.params = params
        self.timestamp = Request.get_timestamp()

    @staticmethod
    def get_timestamp():
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(pytz.timezone('GMT'))
        return date.strftime('%a, %d %b %Y %H:%M:%S ') + 'GMT'

    def get(self):
        uri = self.build_uri(self.params)
        params = ''
        if self.params:
            params += '?{params}'.format(params=urllib.urlencode(self.params.items()))

        headers = self.build_header(self.endpoint + params)
        proxies = self.build_proxy()

        logger.debug('GET - URL: %s' % uri)
        logger.debug('Headers: %s' % uri)
        if proxies:
            logger.debug('Proxies: %s' % proxies)
        response = requests.get(uri,
                                headers=headers,
                                proxies=proxies,
                                timeout=self.config.timeout)
        logger.debug('Response Status: %s' % response.status_code)
        logger.debug('Response: %s' % response.text)

        return Response(response)

    def post(self):
        uri = self.build_uri()
        body = json.dumps(self.params) if self.params else ''
        headers = self.build_header(self.endpoint, body)
        proxies = self.build_proxy()

        logger.debug('POST - URL %s' % uri)
        logger.debug('Body %s', body)
        logger.debug('Headers %s' % uri)
        if proxies:
            logger.debug('Proxies %s' % proxies)
        response = requests.post(uri,
                                 data=body,
                                 headers=headers,
                                 proxies=proxies,
                                 timeout=self.config.timeout)
        logger.debug('Response Status: %s' % response.status_code)
        logger.debug('Response: %s' % response.text)

        return Response(response)

    def patch(self):
        uri = self.build_uri()
        body = json.dumps(self.params) if self.params else ''
        headers = self.build_header(self.endpoint, body)
        proxies = self.build_proxy()

        logger.debug('POST - URL %s' % uri)
        logger.debug('Body %s', body)
        logger.debug('Headers %s' % uri)
        if proxies:
            logger.debug('Proxies %s' % proxies)
        response = requests.patch(uri,
                                  data=body,
                                  headers=headers,
                                  proxies=proxies,
                                  timeout=self.config.timeout)
        logger.debug('Response Status: %s' % response.status_code)
        logger.debug('Response: %s' % response.text)

        return Response(response)

    def build_uri(self, params=None):
        protocol = 'https' if self.config.secure() else 'http'
        url = ''.join([protocol, '://', self.config.host, self.endpoint])
        if params:
            url += '?{params}'.format(params=urllib.urlencode(params.items()))
        return url

    def build_header(self, uri, body=''):
        headers = {
            'User-Agent': VERSION,
            'Accept': 'application/vnd.regalii.v{version}+json'.format(version=self.config.version),
            'Content-type': Request.CONTENT_TYPE,
            'Date': self.timestamp,
            'Content-MD5': Request.content_md5(body),
            'Authorization': self.authorization(uri, body)
        }

        return headers

    def build_proxy(self):
        protocol = 'https' if self.config.secure else 'http'
        auth = '{user}:{password}@'.format(user=self.config.proxy_user,
                                           password=self.config.proxy_pass) if self.config.proxy_user else ''
        proxy = {
            protocol: '{protocol}://{auth}{host}:{port}'.format(protocol=protocol,
                                                                auth=auth,
                                                                host=self.config.proxy_host,
                                                                port=self.config.proxy_port)
        }

        return proxy if self.config.proxy_host else None

    def authorization(self, uri, body):
        secret_key = bytes(self.config.secret_key.encode('utf-8'))
        canonical_string = bytes(self.canonical_string(uri, body).encode('utf-8'))
        hashed = hmac.new(secret_key, canonical_string, sha1)
        auth = b64encode(hashed.digest()).decode('ascii')
        return 'APIAuth {api_key}:{auth}'.format(api_key=self.config.api_key, auth=auth)

    def canonical_string(self, uri, body):
        return ','.join([Request.CONTENT_TYPE, self.content_md5(body), uri, self.timestamp])

    @staticmethod
    def content_md5(body):
        content = ''
        if body:
            m = md5(body)
            content = m.digest().encode("base64").rstrip('\n')

        return content


class BaseClient(object):
    def __init__(self, configuration):
        self.configuration = configuration

    def request(self, endpoint, params=None):
        return Request(self.configuration, endpoint, params)
