from mykopyto import pluck, omit

def test_pluck():
    assert pluck({'a': 1, 'b': 2}, 'a') == {'a': 1}