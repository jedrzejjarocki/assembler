#!/usr/bin/python3

from filesHandler import FilesHandler

def main():
  file_handler = FilesHandler()
  print(file_handler.get_file_data())
  file_handler.write_out()


if __name__ == '__main__':
  main();
