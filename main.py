import requests
import re



url = 'https://www.youtube.com/@hhazem/streams'


def GetLastestStreamId():
    try:
        print('Geting Latest Url')
        html = requests.get(url).text
        id = re.search('(?<="videoId":").*?(?=")', html).group()
        print(id)
        
        
    except Exception as error:
        print(f'Error {error}')
