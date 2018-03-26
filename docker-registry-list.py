#!/usr/bin/env python3
import argparse
import json
import requests


""" Curl examples
curl 'https://auth.docker.io/token?service=registry.docker.io&scope=repository:library/registry:pull'
curl -v https://index.docker.io/v2/library/registry/tags/list -i -H 'Authorization: Bearer {}'
"""


def get_token(auth_url, image_name):
    payload = {
        'service': 'registry.docker.io',
        'scope': 'repository:library/{image}:pull'.format(image=image_name)
    }

    r = requests.get(auth_url + '/token', params=payload)
    if not r.status_code == 200:
        print("Error status {}".format(r.status_code))
        raise Exception("Could not get auth token")

    j = r.json()
    return j['token']


def fetch_versions(index_url, token, image_name):
    h = {'Authorization': "Bearer {}".format(token)}
    r = requests.get('{}/v2/library/{}/tags/list'.format(index_url, image_name),
                     headers=h)
    return r.json()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('name', help='Name of image to list versions of')
    p.add_argument('-t', '--token',
                   help='Auth token to use (automatically fetched if not specified)')
    p.add_argument('-i', '--index-url', default='https://index.docker.io')
    p.add_argument('-a', '--auth-url', default='https://auth.docker.io')

    args = p.parse_args()
    token = args.token or get_token(auth_url=args.auth_url, image_name=args.name)

    versions = fetch_versions(args.index_url, token, args.name)
    print(json.dumps(versions, indent=2))
