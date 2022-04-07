ip = '101.011.201.564'
zip = '5000'




def write_to_file():
    f = open('text.txt', 'a')
    f.write(ip + ' ' + zip + '\n')
    f.close()


write_to_file()