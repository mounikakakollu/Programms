#!/usr/bin/env python
from migrate.versioning.shell import main
from config import config
from database import database_url

if __name__ == '__main__':
    main(url=database_url, debug='False', repository='migrations')
