from mykopyto import omit, IfColEmpty, IfColEq

def test_should_pick_given_key():
    assert omit({'a': 1, 'b': 2}, 'b') == {'a': 1}

def test_should_pick_given_key_from_list_of_dicts():
    assert omit([{'a': 1, 'b': 2}, {'b': 13, 'c': 'ok'}], 'b') == [{'a': 1}, {'c': 'ok'}]

def test_omit_if_all_empty():
    data = [{'a': None, 'b': 2}, {'b': 4}]
    assert omit(data, IfColEmpty('a')) == [{'b': 2}, {'b': 4}]

def test_omit_if_all_empty_empty_strings_retained():
    data = {'a': ''}
    assert omit(data, IfColEmpty('a')) == {'a': ''}

def test_omit_if_all_empty_empty_strings_omitted_when_asked():
    data = {'a': ''}
    assert omit(data, IfColEmpty('a', empty_string_as_empty=True)) == {}

def test_should_keep_key_specified_as_omit_if_all_empty_when_non_empty_values():
    data = [{'a': None, 'b': 2}, {'a': 1, 'b': 4}]
    assert omit(data, IfColEmpty('a')) == data

def test_omit_all_empty_attached_class_style():
    data = [{'a': None, 'b': None, 'c': 'present'}, {'a': None, 'b': None, 'd': None}]
    assert omit(data, omit.AllEmptyCols()) == [{'c': 'present'}, {}]

def test_omit_all_empty_function_property_style():
    data = [{'a': None, 'b': None, 'c': 'present'}, {'a': None, 'b': None, 'd': None}]
    assert omit(data, omit.AllEmptyCols) == [{'c': 'present'}, {}]

def test_omit_all_empty_strings_preservered_by_default():
    data = {'a': None, 'b': ''}
    assert omit(data, omit.AllEmptyCols) == {'b': ''}

def test_omit_all_empty_strings_removed_when_asked():
    data = {'a': None, 'b': ''}
    assert omit(data, omit.AllEmptyCols(empty_string_as_empty = True)) == {}

def test_omit_if_all_eq():
    data = [{'a': 1, 'b': 2}, {'a': 1, 'b': 4}]
    assert omit(data, IfColEq('a', 1)) == [{'b': 2}, {'b': 4}]

def test_omit_if_all_eq_should_keep_when_actually_not_all_eq():
    data = [{'a': 1, 'b': 2}, {'a': 2, 'b': 4}]
    assert omit(data, IfColEq('a', 1)) == data  # should not omit

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
        , omit.IfColEmpty('all_empty_indeed')
        , omit.IfColEmpty('stay_some_values')
        
        ) == [
            {'id': '1', 'stay_some_values': 'present'},
            {'id': '2', 'stay_some_values': None,},
        ]
    
def test_omit_singular_special_types():
    assert omit(
        {
            'id': '1',
            'unconditionally': 'a simple case like in all the other libs',
            'all_empty_indeed': None,
            'stay_some_values': 'present'
        }
        , 'unconditionally'
        , omit.IfColEmpty('all_empty_indeed')
        , omit.IfColEmpty('stay_some_values')
        
        ) == {'id': '1', 'stay_some_values': 'present'}