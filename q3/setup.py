from setuptools import setup, find_packages

setup(name='Cacher',
      version='0.1',
      url='https://github.com/kimbugp/sampled',
      license='MIT',
      author='Kimbugwe Simon',
      author_email='kimbsimon2@gmail.com',
      description='Sampled packages',
      packages=find_packages(exclude=['tests']),
      long_description=open('readME.md').read(),
      zip_safe=False)
