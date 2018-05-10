from bottle import run, route, static_file

@route('/')
def index():
    return static_file('index.html', 'C:/Users/86546/Desktop/')

@route('/resource/<filename>')
def staticFile(filename):
    return static_file(filename, 'C:/Users/86546/Desktop/')    #改为文件夹绝对路径

run(host='10.163.35.202', port='8080')    #改为ipconfig查询的地址