from collections import OrderedDict
import json

# 在迭代操作的时候它会保持元素被插入时的顺序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])

# 精确控制以 JSON 编码后字段的顺序
print(json.dumps(d))
