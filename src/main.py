import sys
from file_operations import copy_static_files_to_public
from generate_page import generate_pages_recursive

def main():

  basepath = sys.argv[1]
  if not basepath:
    basepath = "\\"
  copy_static_files_to_public("./static", "./docs")

  content_dir = "./content"
  template_path = "./template.html"
  public_dir = "./docs"

  generate_pages_recursive(content_dir, template_path, public_dir, basepath)

main()