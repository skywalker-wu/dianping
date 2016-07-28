import AzureStorageClient
from azure.storage import CloudStorageAccount

# Reference:
# - https://github.com/Azure-Samples/storage-python-getting-started/tree/master/AzureStoragePythonGettingStarted
# - https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-table-storage/

account=None
table_service = None

def Init(name,key):
  global account, table_service
  account = CloudStorageAccount(name,key)
  print("storage account created")
  table_service = account.create_table_service()
  print("table service created")

def EnsureTableExist(name):
  global table_service
  if (table_service.exists(name)): 
    print("table exists")
  else:
    table_service.create_table(name)
    print("table created")

def InsertTable(tablename, pkey, rkey, entity):
  global table_service
  entity['PartitionKey']=pkey
  entity['RowKey']=rkey
  table_service.insert_entity(tablename, entity)

def InsertOrUpdateEntity(tablename, pkey, rkey, entity):
  global table_service
  entity['PartitionKey']=pkey
  entity['RowKey']=rkey
  table_service.insert_or_replace_entity(tablename, entity)


  
