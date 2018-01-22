import requests
import json

headers = {
    'Referer':'http://hd.stheadline.com/news/realtime',
}


res = requests.get('http://hd.stheadline.com/ajax/getMoreInstantNewsOnList.php?cid=d',headers=headers)
print(json.dumps(res.text))
