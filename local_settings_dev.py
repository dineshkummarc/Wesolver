# Local settings for development

from os.path import dirname, join, normpath
db_dir = normpath(dirname(__file__))
db_file = join(db_dir, "dev.db")

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = db_file               # Or path to database file if using sqlite3.
DATABASE_USER = ''                    # Not used with sqlite3.
DATABASE_PASSWORD = ''                # Not used with sqlite3.
DATABASE_HOST = ''                    # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''                    # Set to empty string for default. Not used with sqlite3.