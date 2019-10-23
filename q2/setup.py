from setuptools import setup, find_packages

setup(name='Version Checker',
      version='0.1',
      url='https://github.com/kimbugp/version_checker',
      license='MIT',
      author='Kimbugwe Simon',
      author_email='kimbsimon2@gmail.com',
      description='Find if two versions are greater, equal or less than each other',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
