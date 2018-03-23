import os

def findfile(str,path='.'):
    for f in os.listdir(path):
        fpath=os.path.join(path,f)
        if os.path.isfile(fpath) and str in f:
            print(fpath)
        if os.path.isdir(fpath):
            findfile(str,fpath)

findfile('jnu')
