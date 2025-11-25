from enum import Enum
import re

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block):
  lines = markdown_block.split("\n")

  if markdown_block.startswith("#"):
    count = markdown_block.count("#")
    if count >= 1 and count <= 6:
      return BlockType.HEADING
  elif markdown_block.startswith("```") and markdown_block.endswith("```"):
    return BlockType.CODE
  elif markdown_block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
        return BlockType.PARAGRAPH
    return BlockType.QUOTE
  elif markdown_block.startswith("- "):
    for line in lines:
      if not line.startswith("- "):
        return BlockType.PARAGRAPH
    return BlockType.UNORDERED_LIST
  elif markdown_block.startswith("1. "):
    i = 1
    for line in lines:
      if not line.startswith(f"{i}."):
        return BlockType.PARAGRAPH
      i += 1
    return BlockType.ORDERED_LIST
  else:
    return BlockType.PARAGRAPH
  

def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  cleaned_blocks = []
  for block in blocks:
    if block == "":
      continue
    block = block.strip()
    cleaned_blocks.append(block)
  return cleaned_blocks
