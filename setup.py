from setuptools import setup

setup(name='FeodraGooeyKarma',
      version='0.1',
      description='Fedora gooey karma is a user interface for testers to submit karmas for the packages they\'re testing',
      url='https://pagure.io/fedora-qa/fedora-gooey-karma',
      author='imzubin',
      author_email='zchoudhary.10@gmail.com',
      license='GNU',
      packages=['FeodraGooeyKarma'],
      install_requires=['PyQt5','PySide2'],
      entry_points={
          'console_scripts': ['fedora-gooey-karma=FeodraGooeyKarma.FeodraGooeyKarma:main'],
      },
      zip_safe=False)
