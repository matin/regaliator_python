from regalii.clients import EndPoint

API_VERSION = '3.0'


class Client(object):
    class Account(EndPoint):
        def info(self):
            return self.request('/account').get()

    class Bill(EndPoint):
        def create(self, params=None):
            return self.request('/bills', params).post()

        def show(self, id):
            return self.request('/bills/{id}'.format(id=id)).get()

        def update(self, id, params=None):
            return self.request('/bills/{id}'.format(id=id), params).patch()

        def refresh(self, id):
            return self.request('/bills/{id}/refresh'.format(id=id)).post()

        def pay(self, id, params=None):
            return self.request('/bills/{id}/pay'.format(id=id), params).post()

        def xdata(self, id):
            return self.request('/bills/{id}/xdata'.format(id=id)).get()

        def list(self, params=None):
            return self.request('/bills', params).get()

    class Biller(EndPoint):
        def credentials(self, params=None):
            return self.request('/billers/credentials', params).get()

        def topups(self, params=None):
            return self.request('/billers/topups', params).get()

        def utilities(self, params=None):
            return self.request('/billers/utilities', params).get()

    class Rate(EndPoint):
        def list(self):
            return self.request('/rates').get()

        def history(self):
            return self.request('/rates/history').get()

    class Transaction(EndPoint):
        def list(self, params=None):
            return self.request('/transactions', params).get()

    def __init__(self, configuration):
        self.account = Client.Account(configuration)
        self.bill = Client.Bill(configuration)
        self.biller = Client.Biller(configuration)
        self.rate = Client.Rate(configuration)
        self.transaction = Client.Transaction(configuration)
