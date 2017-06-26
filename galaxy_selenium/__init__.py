"""Top-level of library designed to ease use of Selenium targetting Galaxy.

galaxy_selenium is purposes being designed to depend on Python selenium,
six, pyyaml, and optional pyvirtualdisplay but not galaxy-lib (or any of Galaxy
or Galaxy's test stuff) currently.
"""

__version__ = '17.9.0.dev0'

PROJECT_NAME = "galaxy-selenium"
PROJECT_OWNER = PROJECT_USERAME = "galaxyproject"
PROJECT_URL = "https://github.com/galaxyproject/galaxy-selenium"
PROJECT_AUTHOR = 'Galaxy Project and Community'
PROJECT_EMAIL = 'jmchilton@gmail.com'
RAW_CONTENT_URL = "https://raw.github.com/%s/%s/master/" % (
    PROJECT_USERAME, PROJECT_NAME
)
