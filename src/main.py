from textnode import TextNode, TextType
from file_operations import copy_static_files_to_public

def main():
  copy_static_files_to_public("./static", "./public")

main()