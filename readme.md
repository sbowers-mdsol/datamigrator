#Datamigrator

The datamigrator folder represents code that can be used to read data from an external Oracle database.
The intent is the extract the data, transform it, and then load into a DynamoDB instance on AWS.  The code is written based on the native 
Python 2.7 pre-installed on the Mac.

##Development Environment

###DynamoDB
DynamoDB can be run locally on the Mac
1. Download the latest DynamoDB from AWS Website http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html

2. Unzip the downloaded files, and place them into the desired directory.

3. In the terminal, run the following against the diretory<br>

        java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

###Oracle

There are a number of steps necessary to set up the oracle environment on the mac.
1. Download the Oracle Client from Oracle website http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html
- instantclient-basic-macos.x64-12.1.0.2.0.zip
- instantclient-sdk-macos.x64-12.1.0.2.0.zip

2. Unzip the downloaded files, and place them into the desired directory.

3. In the terminal, create a shortcut for later use in that directory
ln -s libclntsh.dylib.12.1 libclntsh.dylib

3. Modify your .bash_profile
-*Tell cx_Oracle setup.py where to find instantclient libs*
export ORACLE_HOME=/usr/local/opt/instantclient_12_1
-*Set -rpath option to tell gcc to look in ORACLE_HOME when linking*
export FORCE_RPATH=1

4. Download and install Oracle
pip install cx_Oracle

5. Verify install
python -c "import cx_Oracle"
If this fails then you may see the following exception:
    >  Traceback (most recent call last):
  File "<string>", line 1, in <module>
  ImportError: dlopen(/Library/Python/2.7/site-packages/cx_Oracle.so, 2): Library not loaded: @rpath/libclntsh.dylib.12.1
  Referenced from: /Library/Python/2.7/site-packages/cx_Oracle.so
  Reason: image not found
  If you are seeing this exception, you either skipped 
  setting ORACLE_HOME and FORCE_RPATH (as described above), 
  or you are using a cached version of the cx_Oracle build 
  when installing. <br><br>
  To force pip to re-build the package, run the following:
  >     pip install --no-cache-dir --allow-external --allow-unverified cx_oracle
  

##Files
###root directory
- .gitignore: Files and directories to be excluded from repository
- _config.ini: Configuration variables
- extractor.py: Extract data from Oracle
- loader.py: Loads data into Dynamo DB
- readme.md: Documentation

###sharedlibs
- config.py: loads configuration from _config.ini file
- debug.py: debugging methods
- tools_dynamo.py: interface with DynamoDB
- tools_http.py: methods for REST
- tools_oracle: interface with OracleDB

###tests
- test_dependencies.py: unit testing that dependencies are installed correctly
- test_dynamo.py: Mock testing of DynamoDB 
- test_extractor.py: Testing the OracleDB connection