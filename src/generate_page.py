import os
from pathlib import Path
from markdown_to_html import markdown_to_html_node



def extract_title(markdown):
  split_markdown = markdown.split("\n")

  for line in split_markdown:
    if line.startswith("#"):
      count = 0
      for c in line:
        if c == "#":
          count += 1
        else:
          break
      if count == 1:
        cleaned_line = line.lstrip("# ").strip()
        return cleaned_line
    
  raise Exception("Error: no h1 heading found")


def generate_page(from_path, template_path, dest_path, basepath):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")

  if not os.path.exists(from_path):
      raise FileNotFoundError("Error: cannot find source file")

  with open(from_path, "r") as file:
    markdown_string = file.read()

  if not os.path.exists(template_path):
    raise FileNotFoundError("Error: cannot find template file")

  with open(template_path, "r") as file:
    template = file.read()

  title = extract_title(markdown_string)
  html_string = markdown_to_html_node(markdown_string).to_html()

  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", html_string)

  template = template.replace('href="/', f'href="{basepath}')
  template = template.replace('src="/', f'src="{basepath}')

  dir_path = os.path.dirname(dest_path)
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)  

  with open(dest_path, "w") as file:
    print(f"Writing to index.html file in {dest_path}...")
    file.write(template)
    print("Write successfull")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
  if not os.path.isdir(dir_path_content):
    raise Exception("Error: content folder not found or invalid")
  for filename in os.listdir(dir_path_content):
    file_path_src = os.path.join(dir_path_content, filename)
    file_path_dest = os.path.join(dest_dir_path, filename)
    if os.path.isdir(file_path_src):
      os.makedirs(file_path_dest, exist_ok=True)
      generate_pages_recursive(file_path_src, template_path, file_path_dest, basepath)
    elif os.path.isfile(file_path_src) and Path(file_path_src).suffix == ".md":
      os.makedirs(dest_dir_path, exist_ok=True)
      dest_html_path = Path(file_path_dest).with_suffix(".html")
      generate_page(file_path_src, template_path, str(dest_html_path), basepath)

      
