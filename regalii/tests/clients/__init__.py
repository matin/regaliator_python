

class ResponseAssertMixin(object):
    def assertResponse(self, r, test_data):
        data = r.data()
        self.assertEqual(r.success(), True)
        self.assertEqual(len(set(data.items()) & set(test_data.items())), len(test_data.keys()))
