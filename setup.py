from setuptools import setup

setup(name='FedoraGooeyKarma',
      version='0.1',
      description='Fedora gooey karma is a user interface for testers to submit karmas for the packages they\'re testing',
      url='https://pagure.io/fedora-qa/fedora-gooey-karma',
      author='imzubin',
      author_email='zchoudhary.10@gmail.com',
      license='GNU',
      packages=['FedoraGooeyKarma'],
      install_requires=['PyQt5'],
      entry_points={
          'console_scripts': ['fedora-gooey-karma=FedoraGooeyKarma.FedoraGooeyKarma:main'],
      },
      zip_safe=False)
