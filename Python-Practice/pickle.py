

import pickle
import pprint

list1 = [1, 2, 3, 4]

pick = pickle.dumps(list1)
print(pick)

unpick = pickle.loads(pick)
print(unpick)



Output:
==>

$python3 main.py
b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04e.'
[1, 2, 3, 4]
