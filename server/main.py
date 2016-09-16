import os
from hashlib import md5
from time import localtime
import subprocess
from bottle import route, run, request, static_file

@route('/')
def root():
    return 'Hello World!'

@route('/upload', method='POST')
def do_upload():
    filename = request.forms.get('filename')
    upload = request.files.get('files')
    name, ext = os.path.splitext(filename)
    if ext not in ['.sdf']:
        print('File extension not allowed')
        return "File extension not allowed."
    else:
        print('File extension allowed')
    save_path = "./upload"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    rand = md5(str(localtime()).encode('utf-8')).hexdigest()
    file_path = '{path}/{md5}_{file}'.format(path=save_path,md5=rand, file=filename)
    upload.save(file_path)
    print('File successfully saved to {}.'.format(file_path))
    file_output_path = '{path}/{md5}_output_{file}.txt'.format(path=save_path,md5=rand, file=filename)
    file_report_path = '{path}/{md5}_report_{file}.txt'.format(path=save_path,mdt=rand, file=filename)
    p = subprocess.Popen(['./Mold2', '-i',file_path,'-o',file_output_path,'-r',file_report_path],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    while p.poll() is None:
        line = p.stdout.readline()
        if line.startswith(b'Finished! Press any key'):
            p.communicate(b'\n')
    print('Finished the Mold2 computation')
    print(file_output_path)
    return static_file(file_output_path,root='.')

if __name__ == '__main__':
    run(host='0.0.0.0', port=9999)
