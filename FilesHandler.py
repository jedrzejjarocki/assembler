import sys
import os.path as path

class FilesHandler():
  def __init__(self):
    self.extension = 'bin'
    self.in_fname = self.get_in_fname()
    self.out = []

  def get_in_fname(self):
    if len(sys.argv) != 2:
      sript_file = path.basename(__file__)
      sys.exit(f'usage: {sript_file} <fname.asm>')

    filename = sys.argv[1]
    if not path.exists(filename):
      sys.exit(f'File {filename} does not exist`');

    return filename

  def get_out_fname(self):
      return path.splitext(self.in_fname)[0] + '.' + self.extension;


  def get_file_data(self):
    with open(self.in_fname, 'r', encoding = 'utf-8') as fi:
      return fi.read().splitlines();

  def write_out(self):
    with open(self.get_out_fname(), 'wb') as fo:
      fo.write(bytearray(''.join(self.out).encode('utf-8')))
