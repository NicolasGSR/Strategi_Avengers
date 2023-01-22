"""Configurações necessarias"""

from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

SECRET_KEY = 'strategi_avengers'

SQLALCHEMY_DATABASE_URI = "postgresql://projeto_strategi_db_user:5AIzRLRsaCBvpGfSv8Bsf2Nk9Ecd8ct9@dpg-cf6ljj1mbjsmchf5vneg-a.oregon-postgres.render.com/projeto_strategi_db"