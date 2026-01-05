## mykopyto 

<img src="./content/logo.svg" alt="logo.svg" style="width:200px;" />

**MYKO**la's **PYT**h**O**n goodies. 

An assorted collection of reusable helpers, probably already better implemented elsewhere or excessive for idiomatic Python. 

Idiosyncratic convenience of use in notebooks a la [marimo](https://marimo.io/) over performance and good habbits ⚠️

## Features 

### omit 

```
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
```

```
    data = [{'a': None, 'b': None, 'c': 'present'}, {'a': None, 'b': None}]
    assert omit(data, AllEmpty()) == [{'c': 'present'}, {}]
```

## -similar- Better art

* [pydash](https://pydash.readthedocs.io/en/latest/api.html) 
* [fnc](https://fnc.readthedocs.io/en/latest/api.html#fnc.utilities.pathgetter)
* [funcy](https://funcy.readthedocs.io/en/stable/cheatsheet.html)