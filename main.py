import sys
from dotenv import dotenv_values

# load username and password for cs council email
secrets = dotenv_values(".env")
username = secrets["username"]
password = secrets["password"]
# load paths to excel sheet and word template, respectively
try:
   details_path = sys.argv[1]
   template_path = sys.argv[2]
except IndexError:
   raise SystemExit("add 2 paths as arguments: path to an excel spreadsheet and path to a word doc template")

def main():
   print(details_path)
   print(template_path)

if __name__ == "__main__":
   main()