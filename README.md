# Regalii Python Client

A Python HTTP client for consuming Regalii's API. The full API docs:

  * Version 3.2 (recommended): https://www.regalii.com/apix/v3/ ;
  * Version 3.1: https://www.regalii.com/api/v3/overview ;
  * Version 3.0: https://www.regalii.com/api/v3/overview ;
  * Version 1.5: https://www.regalii.com/api/v1/overview

## Installation

Add this line to your application's requirements.txt file:

```
git+https://github.com/regalii/regaliator_python.git
```

## Configuration

First of all, you need a `Configuration` instance:

```python

from regalii.configuration import Configuration

config = Configuration(
    # Authentication settings
    'your-api-key',
    'your-secret-key'',

    # API host settings
    'api.casiregalii.com',
    timeout=30,
    use_ssl=True,

    # Proxy settings
    proxy_host=None,
    proxy_port=None,
    proxy_user=None,
    proxy_pass=None,

    # Version target
    version='3.2')
```

## Versions

The available versions are: `1.5`, `3.0`, `3.1` and `3.2` (recommended).

## Requests

**Success:**

```python
> r = Regaliator(config)
> response = r.bill.show(1)
> response.success()
=> True
> response.data()
=> {...}
```

```ruby
> response = r.bill.pay(1, {'amount': 13.0, 'currency': 'MXN'})
> response.success()
=> True
> response.data()
=> {...}
```

**Failure:**

```ruby
> response = r.bill.pay(1, {'amount': 0.0, 'currency': 'MXN'})
> response.success()
=> False
> response.data()
=> {"code": "R3", "message": "Invalid Payment Amount"}
```

## Examples

The following examples will show how to use the Regaliator to connect to the different Regalii API endpoints.

### Billers List
https://www.regalii.com/billers/utilities
```python
response = r.biller.utilities()
```

## Tests

To run the tests, run:
```
$ python setup.py test
```
