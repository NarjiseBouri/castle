import requests
import time
import pprint

URL_BASE = "https://infinite-castles.azurewebsites.net"
CASTLE_MAP = {}


def get_current_room(url, session):
    data = session.get(url).json()
    return data


def get_chests(l_chests, session):
    chests_list = []
    for u in l_chests:
        url = URL_BASE + u
        data = session.get(url).json()
        if 'status' in data and 'empty' not in data['status']:
            chests_list.append(u)
    return chests_list


def fill_castle_mapping(url, session):
    room_name = url.split('/')[-1]
    if room_name in CASTLE_MAP:
        return
    data = get_current_room(url, session)
    room_name = data['id']
    chests = data['chests']
    next_rooms = data['rooms']

    l_full_chests = get_chests(chests, session)
    if len(l_full_chests) > 0:
        CASTLE_MAP[room_name] = {'full_chests': l_full_chests, 'nb_full_chests': len(l_full_chests)}
    for u in next_rooms:
        fill_castle_mapping(URL_BASE + u, session)
    return


if __name__ == '__main__':
    entry_url = URL_BASE + "/castles/1/rooms/entry"
    s = requests.Session()

    start_time = time.time()
    fill_castle_mapping(entry_url, s)
    end_time = time.time()

    print("--- It took {} seconds to find all the chests in the castle---".format(end_time - start_time))

    chests_urls = [v['full_chests'][0] for v in CASTLE_MAP.values()]
    rooms_with_treasure = list(CASTLE_MAP.keys())

    print("\n--- URLs of non-empty chests : ")
    pprint.pp(chests_urls)
    print("\n--- URLs of rooms having non-empty chests : ")
    pprint.pp(rooms_with_treasure)
    print("\n--- Full map of rooms with non empty chests :")
    print(CASTLE_MAP)
