#!/usr/bin/python3

from FilesHandler import FilesHandler

def main():
  file_handler = FilesHandler()
  print(file_handler.get_file_data())


if __name__ == '__main__':
  main();