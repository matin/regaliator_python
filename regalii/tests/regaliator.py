from unittest import TestCase

from regalii.clients import v15, v30, v31
from regalii.configuration import Configuration
from regalii.exceptions import APIVersionError
from regalii.regaliator import Regaliator


class TestRegaliator(TestCase):
    def test_regaliator_default_config(self):
        config = Configuration('a-test-api-key', 'a-test-secret-key', 'a-test-host')
        r = Regaliator(config)
        self.assertIsInstance(r.client, v31.Client)

    def test_regaliator_v15_config(self):
        config = Configuration('a-test-api-key', 'a-test-secret-key', 'a-test-host', version='1.5')
        r = Regaliator(config)
        self.assertIsInstance(r.client, v15.Client)

    def test_regaliator_v30_config(self):
        config = Configuration('a-test-api-key', 'a-test-secret-key', 'a-test-host', version='3.0')
        r = Regaliator(config)
        self.assertIsInstance(r.client, v30.Client)

    def test_regaliator_v31_config(self):
        config = Configuration('a-test-api-key', 'a-test-secret-key', 'a-test-host', version='3.1')
        r = Regaliator(config)
        self.assertIsInstance(r.client, v31.Client)

    def test_regaliator_invalid_verson(self):
        config = Configuration('a-test-api-key', 'a-test-secret-key', 'a-test-host', version='4.0')
        self.assertRaises(APIVersionError, Regaliator, config)
