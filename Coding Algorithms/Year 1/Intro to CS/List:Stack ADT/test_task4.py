import math
import unittest
from test_common import *
import task2
import task4

class TestTask4(unittest.TestCase):
  def test_read(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    self.assertTrue(equal_lines(ed, test_content), msg =  "File not correctly read.")

  def test_print(self):
    pass

  def test_delete(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    ed.delete_num("1")
    self.assertTrue(equal_lines(ed, test_content[1:]), msg =  "Failed to delete first line.")
   
    for index in ["-5"]:
      with self.assertRaises(IndexError, msg = "Deleting out-of-bounds lines should fail."):
        ed.read_filename('TestFile.txt')
        ed.delete_num(index)

    #test cases
    random_text = ['Hi, my name is germaine', 'I study in Monash University', 'I am in the School of IT']
    test1 = task4.Editor()
    test1.read_filename('random.txt')
    test1.delete_num('-1')
    self.assertTrue(equal_lines(test1, random_text[:-1]), msg="Failed to delete last line.")


  def test_insert(self):
    ed = task4.Editor()
    ed.insert_num("1", ToListADT(task2.ListADT, [test_content[0]]))
    self.assertTrue(equal_lines(ed, [test_content[0]]), msg =  "Failed to insert single line.")

    ed = task4.Editor()
    ed.insert_num("-1", ToListADT(task2.ListADT, [test_content[2], test_content[3]]))
    self.assertTrue(equal_lines(ed, [test_content[2], test_content[3]]), msg =  "Incorrect handling of negative insertion")

    #testcases
    test1 = task4.Editor()
    random_text = ['Hi, my name is germaine', 'I study in Monash University','I am in the School of IT']
    test1.insert_num('1',ToListADT(task2.ListADT, [random_text[1], random_text[2]]))
    self.assertFalse(equal_lines(ed, [random_text[1], random_text[2]]), msg =  "Incorrect handling of positive insertion")

    test2 = task4.Editor()
    with self.assertRaises(IndexError, msg='Inserting out of bounds'):
      test2.insert_num('-10', ToListADT(task2.ListADT,[test_content[2], test_content[3]]))



if __name__ == '__main__':
  unittest.main()