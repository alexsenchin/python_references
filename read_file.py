f = open('read.txt')

for line in f:
    data = line.split(':')
    ip = data[0]
    string_port = data[1].split('/')
    port = string_port[0]
    print('IP: ' + ip + ' | ' + 'PORT: ' + port)
    f = open('sokslist.txt', 'a')
    f.write('IP: ' + ip + ' | ' + 'PORT: ' + port)
    f.close()