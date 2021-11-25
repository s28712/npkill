# Import os to get current directory and subdirectories
import os
# Import shutil to remove a directory and all contents
import shutil

# Main function
def main():
  # Get current directory
  directory = os.getcwd()
  # Crawl through all subdirectories
  for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
      # If the subdirectory is node_modules, remove directory
      if subdirectory == "node_modules":
        shutil.rmtree(os.path.join(root, subdirectory))
        
if __name__ == '__main__':
  main()