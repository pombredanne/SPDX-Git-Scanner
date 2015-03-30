These parameters can be passed in via command-line or config file. Most also have a default value if nothing is provided. Parameters are case-insensitive.

To submit them via command line, simply enter any (in any order) as:
<NAME>=<VAL>

If a value has spaces, you will need to wrap it in the quotations appropriate for your os ('' for Linux, "" for Windows).

Adding them via config.txt (located in the same directory as the main script) is mostly the same, except that you do not require quotations for values with spaces.

Command-line parameters have precedence over config parameters, which in turn have precedence over the default values.

Parameters of the form DoSOCS.<param> will override <param> in the DoSOCS config file. Any DoSOCS parameter can be added this way, but the result will be a string variable.

Parameter list:

NAME: TmpDir
DESC: Directory to use for temporary pull down target branch

NAME: TmpZip
DESC: Name to use for temporary package created from branch

NAME: PrintType
DESC: Output type of SPDX file (currently JSON, RDF, and TAG are supported)

NAME: SPDXOutputBase
DESC: Resulting SPDX file base name. PrintType will be appended

NAME: CommitComment
DESC: Comment the script will use when committing the output files. First run through time.strftime(), so format parameters apply.

NAME: Verbose
DESC: Whether or not the script should print what it's doing

NAME: DoSOCS.database_user
DESC: Overrides DoSOCS' database_user parameter

NAME: DoSOCS.database_pass
DESC: Overrides DoSOCS' database_pass parameter

NAME: DoSOCS.database_host
DESC: Overrides DoSOCS' database_host parameter

NAME: DoSOCS.database_port
DESC: Overrides DoSOCS' database_port parameter

NAME: DoSOCS.database_name
DESC: Overrides DoSOCS' database_name parameter

NAME: DoSOCS.FOSSOLOGY_PATH
DESC: Overrides DoSOCS' FOSSOLOGY_PATH parameter

NAME: User
DESC: User name for pushing the SPDX file. If not provided, script will prompt during push.

NAME: Password
DESC: Password for the user pushing the SPDX file. If not provided, script will prompt during push.

NAME: Branch
DESC: Branch for which the script will generate SPDX document file

