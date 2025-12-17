import boto3
from boto3.dynamodb.conditions import Key

def query_movies_by_year(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Movies')

    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response['Items']

if __name__ == '__main__':
    year = 1992
    movies = query_movies_by_year(year)
    print(f"Movies from the year {year}:")
    for movie in movies:
        print(movie)
    print(f"Movies from the year {year}:")
    for movie in movies:
        print(movie)
    print(f"Total movies found: {len(movies)}")