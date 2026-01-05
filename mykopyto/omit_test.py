from mykopyto import omit, IfAllEmpty, AllEmpty, IfAllEq

def test_should_pick_given_key():
    assert omit({'a': 1, 'b': 2}, 'b') == {'a': 1}

def test_should_pick_given_key_from_list_of_dicts():
    assert omit([{'a': 1, 'b': 2}, {'b': 13, 'c': 'ok'}], 'b') == [{'a': 1}, {'c': 'ok'}]

def test_omit_if_all_empty():
    data = [{'a': None, 'b': 2}, {'b': 4}]
    assert omit(data, IfAllEmpty('a')) == [{'b': 2}, {'b': 4}]

def test_should_keep_key_specified_as_omit_if_all_empty_when_non_empty_values():
    data = [{'a': None, 'b': 2}, {'a': 1, 'b': 4}]
    assert omit(data, IfAllEmpty('a')) == data

def test_omit_all_empty():
    data = [{'a': None, 'b': None, 'c': 'present'}, {'a': None, 'b': None}]
    assert omit(data, AllEmpty()) == [{'c': 'present'}, {}]

def test_omit_if_all_eq():
    data = [{'a': 1, 'b': 2}, {'a': 1, 'b': 4}]
    assert omit(data, IfAllEq('a', 1)) == [{'b': 2}, {'b': 4}]

def test_omit_if_all_eq_should_keep_when_actually_not_all_eq():
    data = [{'a': 1, 'b': 2}, {'a': 2, 'b': 4}]
    assert omit(data, IfAllEq('a', 1)) == data  # should not omit

def test_for_docs():
    assert omit([
        {
            'id': '1',
            'unconditionally': 'a simple case like in all the other libs',
            'all_empty_indeed': None,
            'stay_some_values': 'present'
        },
        {
            'id': '2',
            'unconditionally': 'remove as well',
            'stay_some_values': None,
        }]
        , 'unconditionally'
        , omit.IfAllEmpty('all_empty_indeed')
        , omit.IfAllEmpty('stay_some_values')
        
        ) == [
            {'id': '1', 'stay_some_values': 'present'},
            {'id': '2', 'stay_some_values': None,},
        ]