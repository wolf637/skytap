from collections import Iterator
import json
import six
from skytap.framework.ApiClient import ApiClient


class SkytapGroup(ApiClient, six.Iterator):
    def __init__(self):
        super(SkytapGroup, self).__init__()
        self.data = {}
        self.itercount = 0

    def load_list_from_api(self, url, target, params={}):
        self.load_list_from_json(self.rest(url, params), target)
        self.params = params
        self.url = url

    def load_list_from_json(self, json_list, target):
        self.data = {}
        self.target = target

        if isinstance(json_list, str):
            self.json = json.loads(json_list)
        elif isinstance(json_list, list):
            self.json = json_list
        else:
            raise TypeError
        for j in self.json:
            # prefer an int for the ID since that's the most common and
            # easiest to work with, but some things (quotas) have string
            # ids, so we want to leave those alone. A given resource/group
            # will have to handle non-int keys differently if there's a
            # case where that's a problem.
            try:
                self.data[int(j['id'])] = target(j)
            except ValueError:
                self.data[j['id']] = target(j)

    def refresh(self):
        """Reload our data."""
        self.load_list_from_api(self.url,
                                type(list(self.data)[0]),
                                self.params)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        data_str = ''
        for u in self.data:
            data_str += str(self.data[u]) + '\n'
        return data_str

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self

    def __next__(self):
        if self.itercount >= len(self.data):
            raise StopIteration
        n = list(self.data)[self.itercount]
        self.itercount += 1
        return self.data[n]

    def keys(self):
        return self.data.keys()

    def __contains__(self, key):
        return key in self.data
