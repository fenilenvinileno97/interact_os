#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestArrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_double(self):
        testcase = "Marin A., Marlon F."
        expected = "Marlon F. Marin A."
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_single(self):
        testcase = "Voltaire."
        expected = "Voltaire."
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main(verbosity=True)