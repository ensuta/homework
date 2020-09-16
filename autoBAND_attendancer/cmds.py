import os

last_data = input('입력:' )
try:
    if not(os.path.isdir('Log')):
        os.makedirs(os.path.join('Log'))


filepaths = os.path.join('./Log', "log.txt")
fid = open(filepaths, "a")

if not os.path.isfile(filepaths):
    fid.write(last_data)

fid.close()
