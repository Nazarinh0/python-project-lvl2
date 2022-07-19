FLAT_RESULT = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: true
}'''

NESTED_RESULT = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting4: blah blah
      + setting5: {
            key5:value5
        }
        setting6: {
            doge: {
              + wow: so much
              - wow: 1
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      + baz: bars
      - baz: bas
        foo: bar
      + nest: str
      - nest: {'key': 'value'}
    }
  - group2: {
        abc:12345
    }
        deep:{'id': 45}
    }
  + group3: {
        deep:{'id': {'number': 45}}
    }
        fee:100500
    }
}'''

JSON_FORMAT_RESULT = '''{
  "follow": {
    "type": "-",
    "value": "false"
  },
  "host": {
    "type": " ",
    "value": "hexlet.io"
  },
  "proxy": {
    "type": "-",
    "value": "123.234.53.22"
  },
  "timeout": {
    "type": "changed",
    "old_value": 50,
    "new_value": 20
  },
  "verbose": {
    "type": "+",
    "value": "true"
  }
}'''
