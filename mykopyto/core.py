# TODO: proper docs and types
def pluck(dict: dict, *key_names: list[str])->dict:
    return { k:v for k,v in dict.items() if k in key_names}

