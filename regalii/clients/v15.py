from regalii.clients import EndPoint

API_VERSION = '1.5'


class Client(object):
    class Account(EndPoint):
        def info(self):
            return self.request('/account').post()

    class Bill(EndPoint):
        def index(self, params=None):
            return self.request('/bills', params).post()

        def consult(self, params=None):
            return self.request('/bill/consult', params).post()

        def pay(self, params=None):
            return self.request('/bill/pay', params).post()

        def check(self, params=None):
            return self.request('/bill/check', params).post()

    class Biller(EndPoint):
        def topups(self, params=None):
            return self.request('/billers/topups', params).post()

        def utilities(self, params=None):
            return self.request('/billers/utilities', params).post()

    class Rate(EndPoint):
        def list(self):
            return self.request('/rates').post()

        def history(self):
            return self.request('/rates/history').post()

    class Transaction(EndPoint):
        def list(self, params=None):
            return self.request('/transactions', params).post()

        def pay(self, params=None):
            return self.request('/transactions/pay', params).post()

        def reverse(self, params=None):
            return self.request('/transactions/reverse', params).post()

        def cancel(self, params=None):
            return self.request('/transactions/cancel', params).post()

    def __init__(self, configuration):
        self.account = Client.Account(configuration)
        self.bill = Client.Bill(configuration)
        self.biller = Client.Biller(configuration)
        self.rate = Client.Rate(configuration)
        self.transaction = Client.Transaction(configuration)
