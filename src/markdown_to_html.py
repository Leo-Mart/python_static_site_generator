from convert_markdown_block import markdown_to_blocks, block_to_block_type, BlockType
from convert_markdown_inline import text_to_textnodes
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node

# TODO: Clean up? Break out into smaller helpers.
def text_to_children(text):
  child_nodes = []
  nodes = text_to_textnodes(text)
  for node in nodes:
    child_node = text_node_to_html_node(node)
    child_nodes.append(child_node)
  return child_nodes


def markdown_to_html_node(markdown):
  markdown_blocks = markdown_to_blocks(markdown)
  children = []


  for block in markdown_blocks:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
      normalized = " ".join(block.split("\n"))
      node = ParentNode("p", text_to_children(normalized))
    elif block_type == BlockType.HEADING:
      count = 0
      for c in block:
        if c == "#":
          count += 1
        else:
          break   
      tag = f"h{count}"
      heading_text = block[count + 1:]
      node = ParentNode(tag, text_to_children(heading_text))
    elif block_type == BlockType.CODE:
      if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
      lines = block.split("\n")
      lines = lines[1:-1]
      code_text = "\n".join(lines) + "\n"
      code_node = LeafNode("code", code_text)
      node = ParentNode("pre", [code_node])      
    elif block_type == BlockType.QUOTE:
      lines = block.split("\n")
      cleaned_lines = []
      for line in lines:
        if not line.startswith(">"):
          raise ValueError("invalid quote block")
        cleaned_line = line.lstrip("> ").strip()
        cleaned_lines.append(cleaned_line)
      quote_text = " ".join(cleaned_lines)
      node = ParentNode("blockquote", text_to_children(quote_text))
    elif block_type == BlockType.ORDERED_LIST:
      lines = block.split("\n")
      list_item_nodes = []
      for line in lines:
        item_text = line[3:]
        list_item_nodes.append(ParentNode("li", text_to_children(item_text)))
      node = ParentNode("ol", list_item_nodes)
    elif block_type == BlockType.UNORDERED_LIST:
      lines = block.split("\n")
      list_item_nodes = []
      for line in lines:
        item_text = line[2:]
        list_item_nodes.append(ParentNode("li", text_to_children(item_text)))
      node = ParentNode("ul", list_item_nodes) 
      
    children.append(node)
  wrapper_node = ParentNode("div", children=children)
  return wrapper_node

 
