from distutils.core import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
  name = 'Sseugi',         # How you named your package folder (MyLib)
  packages = ['Sseugi'],   # Chose the same as "name"
  version = '0.11',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Romanized Hangul to Hangul converter',   # Give a short description about your library
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Ethan Hill',                   # Type in your name
  author_email = 'ethan.hill1999@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/EHowardHill/sseugi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/EHowardHill/sseugi/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['HANGUL', 'KOREAN', 'ROMANIZATION'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)