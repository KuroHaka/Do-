def get_file_and_write(file_name):
    f = open(file_name,"r")
    g = open("musica.scd","w")
    g.write(f.read())


file = input("Fichero de entrada \n")
get_file_and_write(file) 

 