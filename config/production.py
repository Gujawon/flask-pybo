from logging.config import dictConfig
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x8bp\xaf\x04\xe9.\x14\x9dj\xcf\xe9J\xf63\xa6\xd7'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level' : 'INFO',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes' : 1024 * 1024 * 5, # 5 MB
            'backupCount' : 5,
            'formatter' : 'default',
        },
    },
    'root': {
        'level' : 'INFO',
        'handlers' : ['file']
    }
})

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='}YE7KO$6~N?zsFy`?_6SuSD?5cs%rk__',
    url='ls-98a709f30fddc4971de9d6f531ded8feae235b1f.ckcc3ea6picg.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')