import sys
import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'Topic'
table = dynamodb.Table(table_name)

def handler(event, context):

    logger.info('DELETE topics')

    response = table.delete_item(
        Key={
            'topicId': int(event['pathParameters']['topicID'])
        }
    )

    return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'headers': {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(event['pathParameters']['topicID'])
    }
