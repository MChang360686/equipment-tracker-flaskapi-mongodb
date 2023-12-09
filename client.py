import requests

r = requests.post('http://127.0.0.1:5000/')
print(r.text)

r2 = requests.get('http://127.0.0.1:5000/')
print(r2.text)

"""
printing just the variable only gives us the return code.

You must ask for <varName>.text
"""