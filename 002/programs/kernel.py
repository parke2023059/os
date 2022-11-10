import os
import shutil

version = '0.3'




class Kernel:
    #new folder
    def mkfldr(name, path):
        os.mkdir(path + name)
    #remove folder
    def rmfldr(name, path):
        shutil.rmtree(path + name)
    #rename folder
    #move folder
    #new user
    def mkusr():
        name = str(input('users/'))
        namePath = "users/" + name + "/"
        Kernel.mkfldr(path="users/" , name=name)
        Kernel.mkfldr(path = namePath, name = "Trash")
        Kernel.mkfldr(path = namePath, name = "Workspace")
        Kernel.mkfldr(path = namePath, name = "Documents")
        Kernel.mkfldr(path = namePath, name = "Videos")
        Kernel.mkfldr(path = namePath, name = "Pictures")

    


        
        


  

#login
#sign out




#new user
#remove user
#make file
#remove file
#rename file
#move file
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
