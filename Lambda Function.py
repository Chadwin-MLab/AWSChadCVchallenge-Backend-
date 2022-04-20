import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Web_Visitor_Count')

def lambda_handler(event, context):
    response = table.get_item(Key={
       'Views':'0'
    })
    
    View_Count  = response['Item']['View_Count']
    View_Count = View_Count + 1
    print(View_Count)
    
    response = table.put_item(Item={
            'Views':'0',
            'View_Count': View_Count
    })
    
    return "Records added successfully!"