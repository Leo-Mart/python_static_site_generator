import unittest

from generate_page import extract_title, generate_page

class TestGeneratePage(unittest.TestCase):
  def test_extract_title(self):
    title = extract_title("# Hello")
    self.assertEqual("Hello", title)

  def test_extract_title_extra_spaces(self):
    title = extract_title("#    Hello")
    self.assertEqual("Hello", title)

  def test_extract_title_mutiple_titles(self):
    md = """
# This is a h1 header
This is **bolded** paragraph

### This is a h3 header

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""    
    title = extract_title(md)
    self.assertEqual("This is a h1 header", title)

  def test_extract_title_not_first_line(self):
    md = """
This is **bolded** paragraph

### This is a h3 header

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

# This is a h1 header

- This is a list
- with items
"""    
    title = extract_title(md)
    self.assertEqual("This is a h1 header", title)


  def test_extract_title_no_title(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""   
    
    with self.assertRaises(Exception) as ctx:
      extract_title(md)
    self.assertIn("Error: no h1 heading found", str(ctx.exception))



if __name__ == '__main__':
  unittest.main()