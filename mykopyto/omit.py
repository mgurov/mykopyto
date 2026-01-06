def omit(given: dict, *keys_to_omit):
    """
    Omit specified keys from a dict or a list of dicts.

    The key specification is: 
     - a string (name equality)
     - if_all_empty(key) drops a column when all values are None
     - all_empty() like if_all_empty but for all keys
     - if_all_eq(key, value) if all values of a given key equal to the value
    
    """
    given_list = given if isinstance(given, list) else [given]
    keys_to_omit_processed = set()    
    for spec in keys_to_omit:
        if isinstance(spec, IfAllEmpty):
            if all(d.get(spec.key) is None for d in given_list):
                keys_to_omit_processed.add(spec.key)
        elif isinstance(spec, IfAllEq):
            if all(d.get(spec.key) == spec.value for d in given_list):
                keys_to_omit_processed.add(spec.key)
        elif isinstance(spec, AllEmpty):
            all_keys = set().union(*(d.keys() for d in given_list))
            for key in all_keys:
                if all(d.get(key) is None for d in given_list):
                    keys_to_omit_processed.add(key)
        else:
            keys_to_omit_processed.add(spec)

    if isinstance(given, list):
        return [omit(d, *keys_to_omit_processed) for d in given]
    else:
        return {k: v for k, v in given.items() if k not in keys_to_omit_processed}
    
class IfAllEmpty:
    def __init__(self, key):
        self.key = key

omit.IfAllEmpty = IfAllEmpty

class AllEmpty:
    """
    Removes all keys that have all values empty in all rows 
    """
    pass

omit.AllEmpty = AllEmpty

class IfAllEq:
    def __init__(self, key, value):
        self.key = key
        self.value = value

omit.IfAllEq = IfAllEq
