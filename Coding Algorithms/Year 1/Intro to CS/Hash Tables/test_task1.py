import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task1

class TestTask1(TestCase):
  def test_init(self):
    with self.vis("empty init"):
      x = task1.HashTable()
    with self.vis("init with size and base"):
      z = task1.HashTable(800, 2398)
      
    assert self.check_okay("init")
    
  def test_hash(self):

    x = task1.HashTable(1024, 17)
    for (key, expect) in [("", 0),
                          ("abcdef", 389),
                          ("defabc", 309)]:
        with self.vis():
          self.assertEqual(x.hash(key), expect, msg="Unexpected hash with base 17 and key {key}.")

    assert self.check_okay("hash")

  # The tests for __contains__ and __getitem__ use __setitem__, so we don't make any assumptions
  # about the underlying array representation. Remember to define your own tests for __setitem__
  # (and rehash)
  def test_contains(self):
    x = task1.HashTable(1024, 1)

    with self.vis():
      self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

    with self.vis("unexpected failure in setitem"):
      x["abcdef"] = 18
      x["definitely a string"] = None
      x["abdcef"] = "abcdef"

    for key in ["abcdef", "definitely a string", "abdcef"]:
      with self.vis():
        self.assertTrue(key in x, "False negative in __contains__ for key {}".format(key))

    assert self.check_okay("contains")
  #
  def test_getitem(self):
    x = task1.HashTable(1024, 1)

    with self.vis():
      with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
        elt = x["abcdef"]

    with self.vis("unexpected failure in setitem"):
      x["abcdef"] = 18
      x["definitely a string"] = None

    with self.vis():
      self.assertEqual(x["abcdef"], 18, msg = "Read after store failed.")

    x["abdcef"] = 22

    assert self.check_okay("getitem")

  def test_rehash(self):
    x= task1.HashTable(3,7)
    x["a"]=1
    x["b"]=2
    x["c"]=3
    x["d"]=4
    table_size_new= x.table_size
    with self.vis():
      self.assertEqual(table_size_new,7,msg="rehash failed")
    assert self.check_okay("rehash")


  def test_setitem(self):
    x = task1.HashTable(3,7)
    x["a"] = 1
    x["b"] = 2
    x["c"] = 3
    x["d"] = 4
    assert x.table == [('b', 2), ('c', 3), ('d', 4), None, None, None, ('a', 1)]
    x["e"] = 5
    x["f"] = 6
    assert x.table == [('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), None, ('a', 1)]
    x["a"] = 6
    assert x.table == [('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), None, ('a', 6)]

if __name__ == '__main__':
  unittest.main()
