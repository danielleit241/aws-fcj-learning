import boto3
def delete_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Movies')
    table.delete()
    return table
if __name__ == '__main__':
    movie_table = delete_movie_table()
    print("Table status:", movie_table.table_status)