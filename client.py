import requests

# Make a POST request
r = requests.post('http://127.0.0.1:5000/')
print(r.text)

# Make a GET request
def getPeople(url):
    r = requests.get(url)
    print(r.text)

"""
printing just the variable only gives us the return code.

You must ask for <varName>.text
"""


if __name__ == '__main__':
    getPeople('http://127.0.0.1:5000/')