import mock
import json
from unittest import TestCase

import requests_mock
from regalii import VERSION
from regalii.clients import v15, Request
from regalii.configuration import Configuration
from regalii.tests.clients import ResponseAssertMixin

config = Configuration('api-key',
                       'secret-key',
                       'api.casiregalii.com',
                       version=v15.API_VERSION)

test_date = 'Sun, 1 Jan 2017 12:12:12 GMT'


@requests_mock.Mocker()
class TestClient(ResponseAssertMixin, TestCase):
    @mock.patch('regalii.clients.Request.get_timestamp', return_value=test_date)
    def test_header(self, m, _):
        m.post('https://api.casiregalii.com/account',
               request_headers={
                   'User-Agent': VERSION,
                   'Accept': 'application/vnd.regalii.v{version}+json'.format(version=v15.API_VERSION),
                   'Content-type': Request.CONTENT_TYPE,
                   'Content-MD5': '',
                   'Date': test_date,
                   'Authorization': 'APIAuth api-key:cBkqHFHRxtXiuFhDJMyjk7NwZp0=',
               })

        client = v15.Client(config)
        client.account.info()

    @mock.patch('regalii.clients.Request.get_timestamp', return_value=test_date)
    def test_header_post_params(self, m, _):
        m.post('https://api.casiregalii.com/bills',
               request_headers={
                   'User-Agent': VERSION,
                   'Accept': 'application/vnd.regalii.v{version}+json'.format(version=v15.API_VERSION),
                   'Content-type': Request.CONTENT_TYPE,
                   'Content-MD5': 'Ncu059yzRHSeil5s9h3KoA==',
                   'Date': test_date,
                   'Authorization': 'APIAuth api-key:ia+AJUkNIV9RV+GKgkjPIJJk2q4=',
               })

        client = v15.Client(config)
        client.bill.index({"page": 2})

    def test_data_response(self, m):
        test_data = {
            "name": "ACME Company",
            "balance": 100,
            "minimum_balance": 100,
            "currency": "USD"
        }
        m.post('https://api.casiregalii.com/account',
               text=json.dumps(test_data))
        client = v15.Client(config)
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
        m.post('https://api.casiregalii.com/account',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.account.info()

    # Bill functions
    def test_bill_index(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bills',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.bill.index()

    def test_bill_consult(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bill/consult',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.bill.consult()

    def test_bill_pay(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bill/pay',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.bill.pay()

    def test_bill_check(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/bill/check',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.bill.check()

    # Biller functions
    def test_biller_topups(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/billers/topups',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.biller.topups()

    def test_biller_utilities(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/billers/utilities',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.biller.utilities()

    # Rate functions
    def test_rate(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/rates',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.rate.list()

    def test_rate_history(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/rates/history',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.rate.history()

    # Transaction functions
    def test_transaction(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/transactions',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.transaction.list()

    def test_transaction_pay(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/transactions/pay',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.transaction.pay()

    def test_transaction_reverse(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/transactions/reverse',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.transaction.reverse()

    def test_transaction_cancel(self, m):
        fake_response = {
            "message": "Success",
        }
        m.post('https://api.casiregalii.com/transactions/cancel',
               text=json.dumps(fake_response))
        client = v15.Client(config)
        client.transaction.cancel()
