from unittest import TestCase

from regalii.configuration import Configuration


class TestConfiguration(TestCase):
    def test_configuration_init(self):
        config = Configuration('a-test-api-key', 'a-test-secret-key', 'a-test-host',
                               30, True,
                               'a-test-proxy-host', 'a-test-proxy-port',
                               'a-test-proxy-user', 'a-test-proxy-pass',
                               version='3.1')

        self.assertEqual(config.api_key, 'a-test-api-key')
        self.assertEqual(config.secret_key, 'a-test-secret-key')
        self.assertEqual(config.host, 'a-test-host')
        self.assertEqual(config.timeout, 30)
        self.assertEqual(config.use_ssl, True)
        self.assertEqual(config.secure(), True)
        self.assertEqual(config.proxy_host, 'a-test-proxy-host')
        self.assertEqual(config.proxy_port, 'a-test-proxy-port')
        self.assertEqual(config.proxy_user, 'a-test-proxy-user')
        self.assertEqual(config.proxy_pass, 'a-test-proxy-pass')
        self.assertEqual(config.version, '3.1')
