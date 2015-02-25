import utilities


# Order matters here for deletion.
TABLE_LIST = ["creators", "reviewers", "doc_file_package_associations",
              "licensings", "doc_license_associations", "spdx_docs",
              "package_files", "package_license_info_from_files",
              "packages", "licenses", "spdx_edit_review"]

def emptyTables():
	with utilities.spdxDbConnector() as dbCursor:
  		for table in TABLE_LIST:
  			sqlCmd = "DELETE from " + table
  			dbCursor.execute(sqlCmd)