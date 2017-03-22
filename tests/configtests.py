import datetime
DynamoTestAttributeDefinitions = [
                {
                    'AttributeName': 'oid',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'studyid',
                    'AttributeType': 'N'
                },

        ]

DynamoTestKey = 'oid'
DynamoTestKeyval = 'None'

DynamoTestKeySchema = [
                {
                    'AttributeName': 'oid',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'studyid',
                    'KeyType': 'RANGE'
                }
        ]

DynamoTestProvisionedThroughput = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
        }

DynamoTestQuery = {
                'oid': 'None',
                'studyid': 1,
            }

DynamoTestQuery2 = {
                'oid': 'None',
                'studyid': 2,
            }

DynamoTestRecord = {'oid': 'None', 'studyid': 1, 'info': {'created': '2012-07-18T16:23:15.050000'}}
DynamoTestRecord2 = {'oid': 'None', 'studyid': 2, 'info': {'created': '2014-07-18T16:23:15.050000'}}
DynamoTestRecordUpdated = {'oid': 'None', 'studyid': 1, 'info': {'created': '2013-07-18T16:23:15.050000'}}

DynamoTestRecordset = [
{
                'oid': 'None',
                'studyid': 1,
                'info': {'created': '2012-07-18T16:23:15.050000'}
            },
{
                'oid': 'None',
                'studyid': 2,
                'info': {'created': '2014-07-18T16:23:15.050000'}
            }
]

DynamoTestTablename = "test"
DynamoTestUpdateExpression = "set info.created = :a"
DynamoTestUpdateExpressionAttributeValues = {
        ':a': '2013-07-18T16:23:15.050000'
    }

ODMTestFilename = "testfile"
ODMTestString = '<?xml version="1.0" encoding="utf-8"?><ODM CreationDateTime="2012-07-18T16:23:15.050000" ' \
                'FileOID="SomeFileOID" FileType="Snapshot" Granularity="All" PriorFileOID="SomePriorFileOID" ' \
                'xmlns="http://www.cdisc.org/ns/odm/v1.3" xmlns:ns2="http://www.w3.org/2000/09/xmldsig#">' \
                '<Study OID="None">' \
                '<GlobalVariables>' \
                '<StudyName>SomeStudyName</StudyName>' \
                '<StudyDescription>SomeStudyDescription</StudyDescription>' \
                '<ProtocolName>SomeProtocolName</ProtocolName>' \
                '</GlobalVariables>' \
                '</Study>' \
                '</ODM>'

#<?xml version="1.0" encoding="utf-8"?><ODM CreationDateTime="2012-07-18T16:23:15.050000" FileOID="SomeFileOID" FileType="Snapshot" Granularity="All" PriorFileOID="SomePriorFileOID" xmlns="http://www.cdisc.org/ns/odm/v1.3" xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"><Study OID="None"><GlobalVariables><StudyName>SomeStudyName</StudyName><StudyDescription>SomeStudyDescription</StudyDescription><ProtocolName>SomeProtocolName</ProtocolName></GlobalVariables><BasicDefinitions><MeasurementUnit Name="Kilogram" OID="MU.KG"><Symbol><TranslatedText/></Symbol></MeasurementUnit></BasicDefinitions><MetaDataVersion Name="Version 1.01" OID="v1.01"><Include MetaDataVersionOID="v1.00" StudyOID="123-456-789"/><Protocol><StudyEventRef Mandatory="Yes" OrderNumber="1" StudyEventOID="SE.VISIT0"/></Protocol><StudyEventDef Category="PreTreatment" Name="Pre-treatment" OID="SE.VISIT0" Repeating="No" Type="Scheduled"><FormRef FormOID="FORM.DEMOG" Mandatory="No" OrderNumber="1"/></StudyEventDef><FormDef Name="Adverse Events" OID="FORM.AE" Repeating="No"><ItemGroupRef ItemGroupOID="IG.AE" Mandatory="No" OrderNumber="1"/></FormDef><ItemGroupDef Comment="AE Comment" Domain="AE Domain" IsReferenceData="No" Name="Adverse Events" OID="IG.AE" Origin="AE Origin" Repeating="Yes" Role="AE Role" SASDatasetName="AE"><ItemRef ItemOID="IT.REC_ID" Mandatory="No" OrderNumber="1"/></ItemGroupDef><ItemDef Comment="ABNORM Comment" DataType="integer" Length="2" Name="Normal/Abnormal/Not Done" OID="IT.ABNORM" Origin="ABNORM Origin" SASFieldName="ABNORM" SignificantDigits="1"><Question><TranslatedText xml:lang="en">English: Normal/Abnormal/Not Done?</TranslatedText></Question><ExternalQuestion Code="NormAbnormNotDone" Dictionary="Websters" Version="2001 Unabridged"/><MeasurementUnitRef MeasurementUnitOID="NU.DPML"/><RangeCheck Comparator="LT" SoftHard="Hard"><CheckValue>1</CheckValue><MeasurementUnitRef MeasurementUnitOID="MU.DPML"/><ErrorMessage><TranslatedText xml:lang="en">English: Normal/Abnormal/Not Done?</TranslatedText></ErrorMessage></RangeCheck><CodeListRef CodeListOID="CL.N_A_ND"/><Role>ABNORM Role</Role></ItemDef><CodeList DataType="text" Name="AE Action Taken, Study Drug" OID="CL.AEACTTR" SASFormatName="AEACTTR"><CodeListItem CodedValue="0"><Decode><TranslatedText xml:lang="en">English: Normal/Abnormal/Not Done?</TranslatedText></Decode></CodeListItem></CodeList><Presentation OID="PRS.EN" xml: lang="en">English</Presentation></MetaDataVersion></Study><AdminData StudyOID="123-456-789"><User OID="USR.cdisc001"><FullName>Shirley Williams</FullName><FirstName>Shirley</FirstName><LastName>Williams</LastName><Organization>CDISC</Organization><LocationRef LocationOID="LOC.CDISCHome"/></User><Location LocationType="Site" Name="Roswell Park" OID="LOC.site002"><MetaDataVersionRef EffectiveDate="20011019T10:45:57-05:00" MetaDataVersionOID="v1.01" StudyOID="123-456-789"/></Location><SignatureDef Methodology="Electronic" OID="SD.cdisc001-es"><Meaning>Signature</Meaning><LegalReason>Legal reason</LegalReason></SignatureDef></AdminData><ReferenceData MetaDataVersionOID="v1.01" StudyOID="123-456-789"><ItemGroupData ItemGroupOID="IG.REFSAMP" ItemGroupRepeatKey="1"><ItemData ItemOID="IT.REF1" Value="1"/></ItemGroupData></ReferenceData><ClinicalData MetaDataVersionOID="v1.01" StudyOID="123-456-789"><SubjectData SubjectKey="001"><InvestigatorRef UserOID="USR.inv001"/><SiteRef LocationOID="LOC.site002"/><StudyEventData StudyEventOID="SE.VISIT0"><FormData FormOID="FORM.DEMOG"><Signature><UserRef UserOID="USR.cdisc001"/><LocationRef LocationOID="LOC.CDISCHome"/><SignatureRef SignatureOID="SD.cdisc001-es"/><DateTimeStamp>20010530T10:06:32</DateTimeStamp></Signature><ItemGroupData ItemGroupOID="IG.DEMOG" ItemGroupRepeatKey="1"><ItemData ItemOID="IT.REC_ID" Value="46902604"/></ItemGroupData></FormData></StudyEventData></SubjectData></ClinicalData></ODM>


OracleTestQueryOneRecord = """SELECT O_ID, STUDYID, PROJECTID, CREATED
                        FROM RODS.STUDIES
                        WHERE STUDYID=1 AND rownum=1 """
OracleTestQueryRecordset = """SELECT STUDYID ,PROJECTID, CREATED
                        FROM RODS.STUDIES
                        WHERE rownum < 3 """
OracleTestRecord = {'O_ID': None, 'STUDYID': 1, 'PROJECTID': 2, 'CREATED': datetime.datetime(2012, 7, 18, 16, 23, 15, 50000)}
OracleTestRecordset = [{'STUDYID': 1, 'PROJECTID': 2, 'CREATED': datetime.datetime(2012, 7, 18, 16, 23, 15, 50000)}, {'STUDYID': 2, 'PROJECTID': 3, 'CREATED': datetime.datetime(2012, 7, 18, 16, 32, 41, 773000)}]
