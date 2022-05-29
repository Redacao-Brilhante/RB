from data import populate_database
from database.database import init_database, get_session
import models # noqa


init_database()

session = get_session()

populate_database(session)
