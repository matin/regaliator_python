import mock
import json
from unittest import TestCase

import requests_mock
from regalii import VERSION
from regalii.clients import v31, Request
from regalii.configuration import Configuration
from regalii.tests.clients import ResponseAssertMixin

config = Configuration('api-key',
                       'secret-key',
                       'api.casiregalii.com',
                       version=v31.API_VERSION)

test_date = 'Sun, 1 Jan 2017 12:12:12 GMT'


@requests_mock.Mocker()
class TestClient(ResponseAssertMixin, TestCase):
    @mock.patch('regalii.clients.Request.get_timestamp', return_value=test_date)
    def test_header(self, m, _):
        m.get('https://api.casiregalii.com/account',
              request_headers={
                  'User-Agent': VERSION,
                  'Accept': 'application/vnd.regalii.v{version}+json'.format(version=v31.API_VERSION),
                  'Content-type': Request.CONTENT_TYPE,
                  'Content-MD5': '',
                  'Date': test_date,
                  'Authorization': 'APIAuth api-key:cBkqHFHRxtXiuFhDJMyjk7NwZp0=',
              })

        client = v31.Client(config)
        client.account.info()

    @mock.patch('regalii.clients.Request.get_timestamp', return_value=test_date)
    def test_header_get_params(self, m, _):
        m.get('https://api.casiregalii.com/bills?page=2',
              request_headers={
                  'User-Agent': VERSION,
                  'Accept': 'application/vnd.regalii.v{version}+json'.format(version=v31.API_VERSION),
                  'Content-type': Request.CONTENT_TYPE,
                  'Content-MD5': '',
                  'Date': test_date,
                  'Authorization': 'APIAuth api-key:STh6oN8xVXjtuw4OcSKraYKrzuo=',
              })

        client = v31.Client(config)
        client.bill.list({'page': 2})

    @mock.patch('regalii.clients.Request.get_timestamp', return_value=test_date)
    def test_header_post_params(self, m, _):
        m.post('https://api.casiregalii.com/bills',
               request_headers={
                   'User-Agent': VERSION,
                   'Accept': 'application/vnd.regalii.v{version}+json'.format(version=v31.API_VERSION),
                   'Content-type': Request.CONTENT_TYPE,
                   'Content-MD5': 'Ilbcl2g1pg0HM6IhZrAoow==',
                   'Date': test_date,
                   'Authorization': 'APIAuth api-key:Co1ZsmgTbUPUKhmO6KMcIMERHHw=',
               })

        client = v31.Client(config)
        client.bill.create({"biller_id": 37, "account_number": "4222422244"})

    @mock.patch('regalii.clients.Request.get_timestamp', return_value=test_date)
    def test_header_patch_params(self, m, _):
        m.patch('https://api.casiregalii.com/bills/10',
                request_headers={
                    'User-Agent': VERSION,
                    'Accept': 'application/vnd.regalii.v{version}+json'.format(version=v31.API_VERSION),
                    'Content-type': Request.CONTENT_TYPE,
                    'Content-MD5': '3BEWLu/j40CHTOKvxiNSoA==',
                    'Date': test_date,
                    'Authorization': 'APIAuth api-key:dmB6JzS3/j5DmXcvyc006o6Hqo8=',
                })

        client = v31.Client(config)
        client.bill.update(10, {"account_number": "4222422244"})

    def test_data_response(self, m):
        test_data = {
            "name": "ACME Company",
            "balance": 100,
            "minimum_balance": 100,
            "currency": "USD"
        }
        m.get('https://api.casiregalii.com/account',
              text=json.dumps(test_data))
        client = v31.Client(config)
        r = client.account.info()
        self.assertResponse(r, test_data)


@requests_mock.Mocker()
class TestAccount(TestCase):
    # Purpose of this test is make sure the function call to correct API

    # Account functions
    def test_account_info(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/account',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.account.info()

    # Bill functions
    def test_bill_create(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bills',
               text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.create()

    def test_bill_show(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/bills/1',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.show(1)

    def test_bill_update(self, m):
        fake_response = {
            "message": "Success",
        }
        m.patch('https://api.casiregalii.com/bills/1',
                text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.update(1)

    def test_bill_refresh(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bills/1/refresh',
               text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.refresh(1)

    def test_bill_pay(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bills/1/pay',
               text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.pay(1)

    def test_bill_xdata(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/bills/1/xdata',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.xdata(1)

    def test_bill_list(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/bills',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.list()

    def test_bill_list_page(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/bills?page=2',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.bill.list({'page': 2})

    # Biller functions
    def test_biller_credentials(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/billers/credentials',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.biller.credentials()

    def test_biller_topups(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/billers/topups',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.biller.topups()

    def test_biller_utilities(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/billers/utilities',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.biller.utilities()

    # Rate functions
    def test_rate(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/rates',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.rate.list()

    def test_rate_history(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/rates/history',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.rate.history()

    # Transaction functions
    def test_transaction(self, m):
        fake_response = {
            "message": "Success",
        }
        m.get('https://api.casiregalii.com/transactions',
              text=json.dumps(fake_response))
        client = v31.Client(config)
        client.transaction.list()

