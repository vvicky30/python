
#!/usr/bin/python3

import  boto3
#connecting 
dynamodb=boto3.resource('dynamodb')
# creating table
table=dynamodb.create_table(
        TableName='adhocnewtablee',
        KeySchema=[
            {
                'AttributeName':'username',
                 'KeyType':'HASH'
                
            },
            {
                'AttributeName':'lastname',
                 'KeyType':'RANGE'
                
            }
            
        ],
        AttributeDefinitions=[
           {
               'AttributeName':'username',
               'AttributeType':'S'
               
               },    
           {
               'AttributeName':'lastname',
               'AttributeType':'S'
               
               }    
        ], 
        ProvisionedThroughput={
            'ReadCapacityUnits':1,
            'WriteCapacityUnits':1
            
            }
        
)

table.meta.client.get_waiter('table_exists').wait(TableName='adhocnewtablee')
print(table.item_count)