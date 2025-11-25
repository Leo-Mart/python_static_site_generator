import unittest
from convert_markdown_block import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownConvertBlock(unittest.TestCase):
  def test_markdown_to_blocks(self):
      md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""                                                                             
      blocks = markdown_to_blocks(md)
      self.assertEqual(
          blocks,
          [
              "This is **bolded** paragraph",
              "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
              "- This is a list\n- with items",
          ],
      )

  def test_markdown_to_blocks_newlines(self):
      md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
      blocks = markdown_to_blocks(md)
      self.assertEqual(
          blocks,
          [
              "This is **bolded** paragraph",
              "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
              "- This is a list\n- with items",
          ],
      )


  def test_block_to_blocktype(self):
     md_block = "### This is a heading"
     self.assertEqual(
        block_to_block_type(md_block),
        BlockType.HEADING
     )
     md_block = "> this is the start of the quote block\n>this is another line in the quoteblock"
     self.assertEqual(
        block_to_block_type(md_block),
        BlockType.QUOTE
     )
     md_block = "- an unordered list\n- with some item"
     self.assertEqual(
        block_to_block_type(md_block),
        BlockType.UNORDERED_LIST
     )
     md_block = "1. ordered list\n2. with an item"
     self.assertEqual(
        block_to_block_type(md_block),
        BlockType.ORDERED_LIST
     )
     md_block = "``` This is a code-block ```"
     self.assertEqual(
        block_to_block_type(md_block),
        BlockType.CODE
     )
     md_block = "This is some text that should become a paragraph"
     self.assertEqual(
        block_to_block_type(md_block),
        BlockType.PARAGRAPH
     )

if __name__ == "__main__":
   unittest.main()