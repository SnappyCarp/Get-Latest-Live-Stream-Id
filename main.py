import requests
import re


#Enter Channel Url Here(Must End With /streams)
url = 'https://www.youtube.com/@LofiGirl/streams'


def GetLastestStreamId():
    try:
        print('Geting Latest Url')
        html = requests.get(url).text
        id = re.search('(?<="videoId":").*?(?=")', html).group()
        print(id)
        
        
    except Exception as error:
        print(f'Error {error}')
        
GetLastestStreamId()
