from file_operations import copy_static_files_to_public
from generate_page import generate_page

def main():
  copy_static_files_to_public("./static", "./public")

  from_path = "./content/index.md"
  template_path = "./template.html"
  dest_path = "./public/index.html"

  generate_page(from_path, template_path, dest_path)

main()