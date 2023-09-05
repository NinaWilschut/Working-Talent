print('Start api uitlees applicatie')

import requests as rq

res = rq.get('https://catfact.ninja/facts')
print(res)

feitjes = res.json()