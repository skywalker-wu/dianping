import AzureStorageClient
from azure.storage import CloudStorageAccount

# Reference:
# - https://github.com/Azure-Samples/storage-python-getting-started/tree/master/AzureStoragePythonGettingStarted
# - https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-table-storage/

account=None
table_service = None
table_name = None

def Init(name,key):
  global account, table_service
  account = CloudStorageAccount(name,key)
  print("storage account created")
  table_service = account.create_table_service()
  print("table service created")

def EnsureTable(table):
  global table_service, table_name
  
  table_name = table

  if (table_service.exists(table_name)): 
    print("table exists %s" % table_name)
  else:
    table_service.create_table(table_name)
    print("table created %s" % table_name)

def Update(pkey, rkey, entity):
  global table_service, table_name

  if (table_name == None):
    print("please init table_name")

  entity['PartitionKey']=pkey
  entity['RowKey']=rkey
  table_service.insert_or_replace_entity(table_name, entity)


  
