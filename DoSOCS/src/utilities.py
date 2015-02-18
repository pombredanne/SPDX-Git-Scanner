import settings
import MySQLdb

def spdxDbConnector():
	return MySQLdb.connect(host=settings.database_host,
                           user=settings.database_user,
                           passwd=settings.database_pass,
                           db=settings.database_name)

