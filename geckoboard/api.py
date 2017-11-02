"""
Private: api access methods
"""

import http_requests

API_HOST = 'https://api.geckoboard.com'


def get(path, api_key):
    return http_requests.get(API_HOST + path, auth=(api_key, ''))


def delete(path, api_key):
    return http_requests.delete(API_HOST + path, auth=(api_key, ''))


def post(path, body, api_key):
    return http_requests.post(API_HOST + path, json=body, auth=(api_key, ''))


def put(path, body, api_key):
    return http_requests.put(API_HOST + path, json=body, auth=(api_key, ''))
