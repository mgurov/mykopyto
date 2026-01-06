from typing import Sized


def omit(given: dict, *keys_to_omit):
    """
    Omit specified keys from a dict or a list of dicts.

    The key specification is: 
     - a string (name equality)
     - omit.IfAllEmpty(key) drops a column when all values are None
     - omit.AllEmptyCols() like IfAllEmpty but for all keys; omit.AllEmptyCols(empty_string_as_empty=True) considers treats strings as None
     - omit.IfColEq(key, value) if all values of a given key equal to the value
    
    """
    given_list = given if isinstance(given, list) else [given]
    keys_to_omit_processed = set()    
    for spec in keys_to_omit:
        if isinstance(spec, IfColEmpty):
            if all(spec.is_value_empty(d.get(spec.key)) for d in given_list):
                keys_to_omit_processed.add(spec.key)
        elif isinstance(spec, IfColEq):
            if all(d.get(spec.key) == spec.value for d in given_list):
                keys_to_omit_processed.add(spec.key)
        elif spec == AllEmptyCols or isinstance(spec, AllEmptyCols):
            if spec == AllEmptyCols:
                spec = AllEmptyCols()
            all_keys = set().union(*(d.keys() for d in given_list))
            for key in all_keys:
                if all(spec.is_value_empty(d.get(key)) for d in given_list):
                    keys_to_omit_processed.add(key)
        else:
            keys_to_omit_processed.add(spec)

    if isinstance(given, list):
        return [omit(d, *keys_to_omit_processed) for d in given]
    else:
        return {k: v for k, v in given.items() if k not in keys_to_omit_processed}
    

class WithExtraEmptyFiltering: 
    def __init__(self, empty_string_as_empty: bool=False, empty_list_as_empty: bool=False):
        self.empty_string_as_empty = empty_string_as_empty
        self.empty_list_as_empty = empty_list_as_empty

    def is_value_empty(self, value):
        if value is None:
            return True
        if self.empty_string_as_empty and value == '':
            return True
        if self.empty_list_as_empty and isinstance(value, Sized) and len(value) == 0:
            return True
        return False

class IfColEmpty(WithExtraEmptyFiltering):
    def __init__(self, key, empty_string_as_empty: bool=False, empty_list_as_empty: bool=False):
        super().__init__(empty_string_as_empty, empty_list_as_empty)
        self.key = key
    

class AllEmptyCols(WithExtraEmptyFiltering):
    # """
    # Removes all keys that have all values empty in all rows 
    # """
    pass



class IfColEq:
    def __init__(self, key, value):
        self.key = key
        self.value = value

omit.IfColEmpty = IfColEmpty
omit.AllEmptyCols = AllEmptyCols
omit.IfColEq = IfColEq
