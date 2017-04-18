from subprocess import call
from shutil import make_archive

dir = "testdir"
make_archive(dir, 'zip', root_dir=dir)

