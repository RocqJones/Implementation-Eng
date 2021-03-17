import requests

def fetchData(url):
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise ApiError('GET /products/all/ {}'.format(resp.status_code))
    else:
        for items in resp.json():
            print(items)

if __name__ == '__main__':
    base_url = "https://rocqjones.pythonanywhere.com/api/products/all"
    fetchData(base_url)