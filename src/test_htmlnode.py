import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

  def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

if __name__ == "__main__":
  unittest.main()