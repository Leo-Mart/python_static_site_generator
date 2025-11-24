import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    split_string = old_node.text.split(delimiter)
    if len(split_string) % 2 == 0:
      raise ValueError("invalid markdown, formatted section not closed properly.")
    for i in range(len(split_string)):
      if split_string[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(split_string[i], TextType.TEXT))
      else:
        split_nodes.append(TextNode(split_string[i], text_type)) 
    new_nodes.extend(split_nodes)
  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    if old_node.text is None:
      continue
    original_text = old_node.text
    remaining_text = original_text
    images = extract_markdown_images(original_text)
    split_nodes = []
    for image in images:
      image_alt, image_link = image
      
      sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
      if len(sections) != 2:
        raise ValueError("invalid markdown, image section not closed")
      if sections[0] != "":
        split_nodes.append(TextNode(sections[0], TextType.TEXT))
        
      split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
      remaining_text = sections[1]

    if remaining_text != "":
      split_nodes.append(TextNode(remaining_text, TextType.TEXT))
    new_nodes.extend(split_nodes)

  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    if old_node.text is None:
      continue
    original_text = old_node.text
    remaining_text = original_text
    links = extract_markdown_links(original_text)
    split_nodes = []
    for link in links:
      anchor_text, link_url = link
      sections = remaining_text.split(f"[{anchor_text}]({link_url})", 1)
      if len(sections) != 2:
        raise ValueError("invalid markdown, link section not closed")
      if sections[0] != "":
        split_nodes.append(TextNode(sections[0], TextType.TEXT))
      split_nodes.append(TextNode(anchor_text, TextType.LINK, link_url))
      remaining_text = sections[1]
    if remaining_text != "":
      split_nodes.append(TextNode(remaining_text, TextType.TEXT))
    new_nodes.extend(split_nodes)
  return new_nodes
    

def extract_markdown_images(text):
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches


def extract_markdown_links(text):
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches