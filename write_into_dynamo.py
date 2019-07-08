#!/usr/bin/python3

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('adhocnewtablee')

table.put_item(
   Item={
        'username': 'redashu',
        'first_name': 'google',
        'lastname': 'india',
        'age': 27
    }
)

