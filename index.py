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

    logger.info('DELETE /api/v1/topics/{topicID}')

    response = table.delete_item(
        Key={
            'topicId': int(event['pathParameters']['topicID'])
        }
    )

    return {
            'statusCode': 200,
            'headers': {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
            },
            'body': json.dumps(event['pathParameters']['topicID'])
    }
