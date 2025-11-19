import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode("img", None, None, {"src": "url/to/image"})

    self.assertEqual(
      ' src="url/to/image"', node.props_to_html()
    )

  def test_repr(self):
    node = HTMLNode(
      "p",
      "Some text in here",
      None,
      {"class": "primary"}
    )

    self.assertEqual(
      node.__repr__(), 
      "HTMLNode(p, Some text in here, children: None, {'class': 'primary'})"
    )

  def test_multiple_props(self):
    node = HTMLNode("a", None, None, {"href": "https://www.test.com", "target": "_blank"})

    self.assertEqual(
      ' href="https://www.test.com" target="_blank"', node.props_to_html()
    )

  def test_no_prop(self):
    node = HTMLNode("img", None, None, None)

    self.assertEqual("", node.props_to_html())

  def test_values(self):
    node = HTMLNode(
      "div",
      "Some text in a div",
    )

    self.assertEqual(
      node.tag,
      "div"
    )

    self.assertEqual(
      node.value,
      "Some text in a div"
    )

    self.assertEqual(
      node.children,
      None
    )

    self.assertEqual(
      node.props,
      None
    )