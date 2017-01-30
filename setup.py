from setuptools import setup

setup(name='reagliator_python',
      version='1.0.0',
      description="A Python HTTP client for consuming Regalii's API",
      url='https://github.com/regalii/regaliator_python',
      author='Regalii',
      author_email='support@regalii.com',
      license='MIT',
      packages=['regalii'],
      install_requires=[
          'pytz',
          'requests',
          'mock',
          'requests-mock'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
