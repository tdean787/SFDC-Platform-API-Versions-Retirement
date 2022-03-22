## Salesforce Platform API Versions 7.0 through 20.0 Retirement

### A Guide to Programmatic Validation of Salesforce Applications Consuming Legacy API Versions

Per the Salesforce Release Update as of the Summer '21 Release, API versions 7.0 to 20.0 will become retired and unavailable.

In order to identify applications within your Salesforce org that are using legacy versions, this script was created to expedite the querying of event log files.

The high level steps needed to use this and check your log files is as follows:

1. Run the SOQL query on EventLogFile object: 
    sfdx force:data:soql:query -q "SELECT LogFile, EventType, CreatedDate FROM EventLogFile WHERE EventType IN ('API', 'RestApi', 'ApiTotalUsage')" -u <your-username>
2. Collect the list of endpoints you receive from the above query and turn them into an array to include in request.py for the endpoints variable
3. Set your params for username, password, client_id, and client_secret
    Page 22 of this guide http://www.salesforce.com/us/developer/docs/api_rest/api_rest.pdf has details on acquiring your client key and secret
4. Set your domain and the save path within the function
5. You will end with a collection of csv files that you can then search through for any API versions that are being retired. Concatenating the files may further speed up the filtering process and minimize the total number of files to click into.
