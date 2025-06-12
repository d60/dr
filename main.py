import time
from datetime import datetime, timedelta

from httpx import Client

from config import config
from utils import build_form_data


class Reserve:
    def __init__(self) -> None:
        self.client = Client()
        self.org_id = config['org_id']
        self.auth_token = config['auth_token']

    def gql_post(self, url, query, variables, operation_name):
        data = {
            'query': query,
            'variables': variables,
            'operationName': operation_name
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post(url, json=data, headers=headers)
        return response

    def get_slots(self, menu_id, from_unix):
        to_unix = from_unix + timedelta(7).total_seconds()
        url = 'https://ttzk.graffer.jp/booth-reserve/api/booth-reserve/graphql/v1/query'
        query = '''query slots($request: SlotRequest!) {\n  slots(request: $request) {\n    slotPerDates {\n      slots {\n        startAtUnixSecond\n        endAtUnixSecond\n        maxReceiveCount\n        availableReceiveCount\n      }\n    }\n  }\n}'''
        variables = {
            'request': {
                'menuId': menu_id,
                'orgId': self.org_id,
                'fromUnixSecond': int(from_unix),
                'toUnixSecond': int(to_unix)
            }
        }
        return self.gql_post(url, query, variables, 'slots').json()

    def reserve(self, from_unix, to_unix, menu_id):
        url = 'https://ttzk.graffer.jp/booth-reserve/api/booth-reserve/portal/v1/reservations'
        form_data = build_form_data(from_unix, to_unix, menu_id)
        headers = {'Content-Type': 'application/json'}
        cookies = {'graffer_auth': self.auth_token}
        return self.client.post(url, json=form_data, headers=headers, cookies=cookies)


r = Reserve()
MORIYAMA_MENU_ID = config['moriyama_menu_id']
MAIBARA_MENU_ID = config['maibara_menu_id']

PRIORITIES = [
    [datetime(2025, 6, 16, 8, 30), MORIYAMA_MENU_ID],
    [datetime(2025, 6, 19, 8, 30), MORIYAMA_MENU_ID],
    [datetime(2025, 6, 19, 8, 30), MAIBARA_MENU_ID],
    [datetime(2025, 6, 26, 8, 30), MAIBARA_MENU_ID],
]

def find_slot(ts, data):
    for date in data['data']['slots']['slotPerDates']:
        for slot in date['slots']:
            if slot['startAtUnixSecond'] == ts:
                return slot

def main():
    for dt, menu_id in PRIORITIES:
        ts = int(dt.timestamp())
        rs = r.get_slots(menu_id, ts)
        slot = find_slot(ts, rs)
        print(slot)
        if slot['availableReceiveCount'] == 0:
            continue
        r.reserve(slot['startAtUnixSecond'], slot['endAtUnixSecond'], menu_id)
        return dt, menu_id


while True:
    result = main()
    if result:
        print(result)
        break
    print('=====================')
    time.sleep(1*30)
