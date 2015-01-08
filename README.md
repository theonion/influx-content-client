
```

>>> from influx_content_client import ContentClient
>>>
>>> client = ContentClient('localhost', 8086, 'root', 'root', 'db', 'avclub')
>>> content_objects = client.get_content('1d')
>>> for content in content_objects:
...     print(content)
...
[avclub] 213160: 984
[avclub] 213549: 858
[avclub] 211215: 852
[avclub] 13861: 735
[avclub] 213408: 457
[avclub] 213087: 274
[avclub] 213447: 224
[avclub] 213563: 202
[avclub] 212785: 185
[avclub] 213520: 161
[avclub] 213174: 142
[avclub] 213566: 140
[avclub] 103462: 139
[avclub] 208514: 101
[avclub] 107422: 91

>>>
>>> client = ContentClient('localhost', 8086, 'root', 'root', 'db', 'clickhole')
>>> content_objects = client.get_content('1d', limit=3)
>>> for content in content_objects:
...     print(content)
...
[clickhole] 1655: 9124
[clickhole] 1648: 1745
[clickhole] 1138: 1663

```
