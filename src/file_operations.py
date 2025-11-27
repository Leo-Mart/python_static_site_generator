import os
import shutil

def copy_static_files_to_public(source, destination):
  # FIrst delete files from the /public directory to ensure that the copy is clean
  print("Deleting public directory...")
  if os.path.exists(destination):
    shutil.rmtree(destination)

  os.mkdir(destination)

  copy_files(source, destination)

def copy_files(source, destination):
  # copy all files, subdirs, nested files etc
  if not os.path.exists(source):
    raise Exception("Error: static folder was not found")
  for filename in os.listdir(source):
    file_path = os.path.join(source, filename)
    if os.path.isfile(file_path):
      print(f"Copying file: {file_path} to '{destination}'...")
      shutil.copy(file_path, destination)
      print(f"Successfully copied file: {filename}")
    if os.path.isdir(file_path):
      sub_directory = os.path.join(destination, filename)
      os.mkdir(sub_directory)
      print(f"Copying directory: {file_path} to {sub_directory}...")
      copy_files(file_path, sub_directory)
      print(f"Successfully copied folder: {file_path} to {sub_directory}")

  
