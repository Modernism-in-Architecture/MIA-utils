import argparse
import os.path
from time import time

import requests
from requests.auth import AuthBase


class MIAAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers['Authorization'] = f"Token {self.token}"
        return request


def error(message):
    print('\033[38;5;196mERROR: ' + message + '\033[0;0m')


def readToken(tokenFileName="token.txt"):
    if not os.path.exists(tokenFileName):
        error(f"Token file {tokenFileName} does not exist")
        assert False
    with open(tokenFileName, "r") as tokenFile:
        return tokenFile.readline().strip()


def processBuildings(limit=10):
    token = readToken()
    response = requests.get("https://modernism-in-architecture.org/api/v1/buildings/", auth=MIAAuth(token))
    if response.status_code != 200:
        error(f"Cannot process buildings. Server response code: {response.status_code}")
        return

    buildings = response.json()['data']
    for _, building in zip(range(limit), buildings):
        processBuilding(building, token)


def processBuilding(building, token):
    print(f"request building (id: {building['id']:4}) {building['name'][0:30]:<31} ... ", end='')
    startTime = time()
    response = requests.get(f"https://modernism-in-architecture.org/api/v1/buildings/{building['id']}", auth=MIAAuth(token))
    duration = time() - startTime
    print(f"done. [{response.status_code}, {duration:.4f}sec]")


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('maxBuildings', type=int, help='Maximum number of buildings to be queried.')
    return parser.parse_args()


def main():
    args = parse_args()
    processBuildings(args.maxBuildings)


if __name__ == '__main__':
    main()
