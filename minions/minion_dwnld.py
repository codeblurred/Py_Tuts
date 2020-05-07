from idlelib.multicall import r

import requests

chunk_size =  256

url = "https://redirect.veoh.com/flash/p/2/v18766010e5N7HYpF/h18766010.mp4?ct=691dc5aaf36f8eafff869b769ce4c6b6880ff048f45f637d"

r - requests.get(url, stream=True)


with open("vamsfile.mp4", 'wb') as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)




