import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "hello, world!")
    self.assertEqual(node.to_html(), "<p>hello, world!</p>")

  def test_leaf_to_html_a(self):
    node = LeafNode("a", "A link!",{"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">A link!</a>')

  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")