from file_operations import copy_static_files_to_public
from generate_page import generate_pages_recursive

def main():
  copy_static_files_to_public("./static", "./public")

  content_dir = "./content"
  template_path = "./template.html"
  public_dir = "./public"

  generate_pages_recursive(content_dir, template_path, public_dir)

main()