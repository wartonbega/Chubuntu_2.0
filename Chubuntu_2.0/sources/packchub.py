import random
import tkinter as tk
import os
pact = ['IDE','dictionnaire']
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def refresh_pac():
    global installed
    paced=find_pac()
    labtext='paquets installés : \n'
    for names in paced:
        print(names)
        labtext+=names+'\n'
    installed.configure(text=labtext)
    print('bited')

def find_pac():
    paquets_ = os.listdir('./installateur_packet/')
    paquets_installe=[]
    for pacts in paquets_:
        print(pacts)
        for i in range(len(pacts)):
            if pacts[i]=='_':
                paquets_installe.append(pacts[:i])
                break
    return paquets_installe


            
def newname(oldName):
    name = oldName+'_'
    for i in range(100):
        name+=str(random.randint(0,9))
        name+=random.choice(letters)
    files = os.listdir('./installateur_packet/')
    if name in files:
        return newname()
    else:
        return name

def install():
    global name
    name = liste.get(liste.curselection()[0])
    print(name)
    title = 'installation du paquet : '+name
    but.config(text=title)
    git(name)
    
def git(name):
    new_name=newname(name)
    os.popen('svn checkout https://github.com/wartonbega/'+name+'.git /home/appel/Chubuntu_2.0/sources/installateur_packet/','r').read()
    os.popen('mv ./installateur_packet/trunk/'+name+'.py /home/appel/Chubuntu_2.0/sources/'+name+'.py','r')
    os.popen('mkdir ./installateur_packet/'+new_name,'r')
    os.popen('mv ./installateur_packet/.svn ./installateur_packet/'+new_name+'/','r')
    os.popen('mv ./installateur_packet/branches ./installateur_packet/'+new_name+'/','r')
    os.popen('mv ./installateur_packet/trunk ./installateur_packet/'+new_name+'/','r')
    os.popen('mv ./installateur_packet/ ./installateur_packet/'+new_name+'/','r')
    
    but.config(text='installer le paquet seléctionné')
    refresh_pac()
    
window = tk.Tk()
window.title('installateur de paquets packchub')

liste = tk.Listbox(window)
liste.pack()
for names in pact:
    liste.insert(tk.END,names)

but = tk.Button(window,text='installer le paquet séléctionné', command=install)
but.pack(expand='YES')



installed = tk.Label(window, text=labtext)
installed.pack(side='top')
refresh_pac()
window.mainloop()