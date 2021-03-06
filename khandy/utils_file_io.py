import json
from collections import OrderedDict


def load_list(filename, encoding='utf-8', start=0, stop=None):
    assert isinstance(start, int) and start >= 0
    assert (stop is None) or (isinstance(stop, int) and stop > start)
    
    lines = []
    with open(filename, 'r', encoding=encoding) as f:
        for _ in range(start):
            f.readline()
        for k, line in enumerate(f):
            if (stop is not None) and (k + start > stop):
                break
            lines.append(line.rstrip('\n'))
    return lines


def save_list(filename, list_obj, encoding='utf-8', append_break=True):
    with open(filename, 'w', encoding=encoding) as f:
        if append_break:
            for item in list_obj:
                f.write(str(item) + '\n')
        else:
            for item in list_obj:
                f.write(str(item))


def load_json(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as f:
        dict_obj = json.load(f, object_pairs_hook=OrderedDict)
    return dict_obj


def save_json(filename, dict_obj, encoding='utf-8', sort_keys=False):
    with open(filename, 'w', encoding=encoding) as f:
        json.dump(dict_obj, f, indent=4, separators=(',',': '),
                  ensure_ascii=False, sort_keys=sort_keys)

