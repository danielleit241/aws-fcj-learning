from decimal import Decimal
import boto3
from pprint import pprint

def update_movie(title, year, rating, plot, actors, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': Decimal(str(rating)),
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    response = update_movie("The Big New Movie", 2015, 5.5,
                            "Everything happens all at once.",
                            ["Larry", "Moe", "Curly"])
    print("Update movie succeeded:")
    pprint(response, sort_dicts=False)