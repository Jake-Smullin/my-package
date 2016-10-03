# Just a test file to upload to a pypi instance.
from distutils.core import setup

setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  author = 'Jacob Smullin',
  author_email = 'jsmullin@ea.com',
  url = 'https://github.com/Jake-Smullin/my-package', # use the URL to the github repo
  download_url = 'https://github.com/Jake-Smullin/my-package/tarball/0.1', 
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
