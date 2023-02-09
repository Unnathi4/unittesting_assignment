import boto3
import pytest
from botocore.exceptions import ParamValidationError
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample
DynamodBExample_instance = DynamodBExample()

@mock_dynamodb2
def test_create_dynamo_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = DynamodBExample_instance.create_movies_table(dynamodb)
    assert table.name == 'Movies'



@mock_dynamodb2
def test_add_dynamo_record_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = DynamodBExample_instance.create_movies_table(dynamodb)
    result = DynamodBExample_instance.add_dynamo_record_table("Movies", {'year': 2015, 'title': "hello"}, dynamodb)
    assert result['ResponseMetadata']['HTTPStatusCode'] == 200


@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    try:
        with pytest.raises(ParamValidationError):
            table = DynamodBExample_instance.create_movies_table(dynamodb)
            result = DynamodBExample_instance.add_dynamo_record_table("/Movies", {'year': 2015, 'title': "hello"}, dynamodb)

    except:
        print("Invalid Parameter")




