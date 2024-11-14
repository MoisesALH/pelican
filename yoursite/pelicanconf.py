AUTHOR = 'Owen|Moises'
SITENAME = 'Ivan Atimarte'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Atlantic/Canary'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# THEME = 'themes/Flex'

# Blogroll
LINKS = (
    ('Owen', 'https://github.com/OwenHernandez'),
    ('Moises', 'https://github.com/MoisesALH'),
)

# Social widget
SOCIAL = (('Youtube', 'https://www.youtube.com/@ibb007'),)

PAGE_PATHS = ['']
ARTICLE_PATHS = []

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

THEME_TEMPLATES_OVERRIDES = ['templates']
INDEX_SAVE_AS = 'home.html'


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Inicio', '/index.html'),
    ('Servicios', '/servicios.html'),
    ('Acerca de nostros', '/about.html'),
    ('Contacto', '/contacto.html'),
]


CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
