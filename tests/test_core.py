from mykopyto import pluck

def test_pluck():
    assert pluck({'a': 1, 'b': 2}, 'a') == {'a': 1}