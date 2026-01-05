def omit(given: dict, *keys_to_omit):
    """
    Omit specified keys from a dict or a list of dicts.

    The key specification is: 
     - a string (name equality)
     - if_all_empty(key) drops a column when all values are None
     - all_empty() like if_all_empty but for all keys
     - if_all_eq(key, value) if all values of a given key equal to the value
    
    """
    if isinstance(given, list):
        # determine which keys to omit based on the list
        keys_to_omit_expanded = set()
        for spec in keys_to_omit:
            if isinstance(spec, str):
                keys_to_omit_expanded.add(spec)
            elif isinstance(spec, IfAllEmpty):
                if all(d.get(spec.key) is None for d in given):
                    keys_to_omit_expanded.add(spec.key)
            elif isinstance(spec, AllEmpty):
                all_keys = set().union(*(d.keys() for d in given))
                for key in all_keys:
                    if all(d.get(key) is None for d in given):
                        keys_to_omit_expanded.add(key)
            elif isinstance(spec, IfAllEq):
                if all(d.get(spec.key) == spec.value for d in given):
                    keys_to_omit_expanded.add(spec.key)
        return [{k: v for k, v in d.items() if k not in keys_to_omit_expanded} for d in given]
    else:
        # for single dict, only omit string keys
        keys_to_omit_strings = [spec for spec in keys_to_omit if isinstance(spec, str)]
        return {k: v for k, v in given.items() if k not in keys_to_omit_strings}
    
class IfAllEmpty:
    def __init__(self, key):
        self.key = key

class AllEmpty:
    pass

class IfAllEq:
    def __init__(self, key, value):
        self.key = key
        self.value = value
