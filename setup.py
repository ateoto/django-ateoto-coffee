from setuptools import setup

version = __import__('ateoto_coffee').__version__

setup(name = 'django-ateoto-coffee',
    version = version,
    author = 'Matthew McCants',
    author_email = 'mattmccants@gmail.com',
    description = 'Coffee and Tea Preparation helper',
    license = 'BSD',
    url = 'https://github.com/Ateoto/django-ateoto-coffee',
    packages = ['ateoto_coffee'],
    install_requires = ['django>=1.4'])
