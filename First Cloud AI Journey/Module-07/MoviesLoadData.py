from decimal import Decimal
from json import load
import boto3

def load_movies(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        info = movie['info']

        # Convert floats to Decimal for DynamoDB
        if 'rating' in info:
            info['rating'] = Decimal(str(info['rating']))
        if 'votes' in info:
            info['votes'] = Decimal(str(info['votes']))

        table.put_item(
           Item={
                'year': year,
                'title': title,
                'info': info
            }
        )
if __name__ == '__main__':
    with open("moviedata.json") as json_file:
        movie_list = load(json_file, parse_float=Decimal)
        load_movies(movie_list)