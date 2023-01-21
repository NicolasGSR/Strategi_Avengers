"""Configurações necessarias"""

from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

SECRET_KEY = 'strategi_avengers'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'nicolassreis',
        senha = 'senhauser',
        servidor = 'localhost',
        database = 'marvel_db'
    )