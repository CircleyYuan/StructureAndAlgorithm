"""
示例：
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""

import collections

class LRUCache:

    def __init__(self,capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self,key):
        """
        :type key: int
        :retype: int
        """
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val
        return val

    def put(self,key,value):
        """
        :param key: int
        :param value: int
        :return: void
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value