#!/usr/bin/env python3

# Examples from https://urllib3.readthedocs.io/en/latest/user-guide.html
import io
import json
import logging
import urllib3
import certifi

from urllib.parse import urlencode

logging.getLogger("urllib3").setLevel(logging.WARNING)

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.data)
print()

r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={'hello': 'world'})
print(r.data)
print()

r = http.request('GET', 'http://httpbin.org/ip')
print(r.status)
print(r.data)
print(r.headers)
print()

r = http.request('GET', 'http://httpbin.org/ip')
print(json.loads(r.data.decode('utf-8')))
print()

r = http.request('GET', 'http://httpbin.org/bytes/8')
print(r.data)
print()

r = http.request('GET', 'https://example.com', preload_content=False)
r.auto_close = False
for line in io.TextIOWrapper(r):
    print(line)
print()

r = http.request(
    'GET',
    'http://httpbin.org/headers',
    headers={
        'X-Something': 'value'
    })
print(json.loads(r.data.decode('utf-8'))['headers'])
print()

r = http.request(
    'GET',
    'http://httpbin.org/get',
    fields={'arg': 'value'})
print(json.loads(r.data.decode('utf-8'))['args'])
print()

encoded_args = urlencode({'arg': 'value'})
url = 'http://httpbin.org/post?' + encoded_args
r = http.request('POST', url)
print(json.loads(r.data.decode('utf-8'))['args'])
print()

r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={'field': 'value'})
print(json.loads(r.data.decode('utf-8'))['form'])
print()

data = {'attribute': 'value'}
encoded_data = json.dumps(data).encode('utf-8')
r = http.request(
    'POST',
    'http://httpbin.org/post',
    body=encoded_data,
    headers={'Content-Type': 'application/json'})
print(json.loads(r.data.decode('utf-8'))['json'])
print()

with open('example.txt') as fp:
    file_data = fp.read()
fp.close()
r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={
        'filefield': ('example.txt', file_data),
    })
print(json.loads(r.data.decode('utf-8'))['files'])
print()

r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={
        'filefield': ('example.txt', file_data, 'text/plain'),
    })
print(json.loads(r.data.decode('utf-8'))['files'])
print()

with open('example.png', 'rb') as fp:
    binary_data = fp.read()
fp.close()
r = http.request(
    'POST',
    'http://httpbin.org/post',
    body=binary_data,
    headers={'Content-Type': 'image/jpeg'})
# print(json.loads(r.data.decode('utf-8'))['data'])
print()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
http.request('GET', 'https://google.com')
print(r.status)
# print(r.data)
print(r.headers)
print()

try:
    http.request('GET', 'https://expired.badssl.com')
except urllib3.exceptions.MaxRetryError:
    print('SSL failed.')

try:
    http.request('GET', 'nx.example.com', retries=False)
except urllib3.exceptions.NewConnectionError:
    print('Connection failed.')
