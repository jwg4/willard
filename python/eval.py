from subprocess import check_output
from tempfile import NamedTemporaryFile

def get_output(code):
    tmpfile = NamedTemporaryFile()
    tmpfile.write(code)
    tmpfile.flush()
    args = ['python', tmpfile.name]
    output = check_output(args)
    return output
