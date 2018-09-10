import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.mkdirs(directory)


def write_file(path, data):
    fo = open(path, 'w')
    fo.write(data)
    fo.close()
