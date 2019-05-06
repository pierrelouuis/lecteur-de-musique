#!/usr/local/bin/python3

## Windows
# Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

import os
import pygame                         #  Module installé pour contrôler l'audio en streaming
from pygame import mixer
import tkinter                        #  Intégrer à*Python pour l'interface graphique
from tkinter import *
from tkinter.filedialog import *    #  Intégrer à*Python pour chercher et ouvrir des fichiers
import tkinter.filedialog

CURRENT_DIR = os.getcwd()
IMG_DIR = CURRENT_DIR + '/images'
MP3_DIR = CURRENT_DIR + '/mp3' 

def Ouvrir():
    fichier_music = tkFileDialog.askopenfile(title="choisisez un fichier", filetypes=[('mp3 files','.mp3')])
    pygame.mixer.music.load (fichier_music.name)
    listbox.delete (20,END) #Réinitialise la playlist
    listbox.insert(END,filename)

def Liste():
    fichier_music = tkFileDialog.askopenfile(title='choisissez un fichier',filetypes=[('mp3 files', '.mp3')])
    pygame.mixer.music.queue(fichier_music.name)
    listbox.insert(END, fichier_music.name)

def Exit(): #Ferme la page
    Mafenetre.destroy()
    pygame.mixer.music.pause()
     
def Lecture():
    pygame.mixer.music.play()
 
def Pause():
    pygame.mixer.music.pause()
 
def Reprise():
    pygame.mixer.music.unpause()
 
def Vol():
    Mafenetre.after(100,Vol) #Tps actualisation son = 100ms
    Vol_1 = Buttonvolume.get() #valeur volume
    pygame.mixer.music.set_volume(vol1*.01) #donne valeur a variable
    
def Mute():  
    Buttonvolume.set(0) 
 
def Fermer():
    pygame.mixer.music.stop()
    
#  Interface graphique
Mafenetre = Tk ()
Mafenetre.geometry('600x500+400+400')
Mafenetre.configure(bg='black')
Mafenetre.title('Morpheo Musique')
Mafenetre.after(100,Vol) #Rafraichi valeur volume

#definition de l'arriere plan

photo = PhotoImage(file = IMG_DIR + "background.jpg")
Largeur = 500
Hauteur = 300

#Import de la photo et definiton de la zone

Canvas=Canvas(Mafenetre,width=Largeur, height=Hauteur)
item=Canvas.create_image(0,0,anchor=NW, image=photo)
Canvas.pack

#Barre de Menu

menubar = Menu(Mafenetre)
Mafenetre.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Ouvrir", command=import_sound)
filemenu.add_command(label="Ajouter dans playlist", command=playlist)
filemenu.add_separator()
filemenu.add_command(label="Fermer", command=Exit)
menubar.add_cascade(label="Fichier", menu=filemenu)

#curseur volume

Buttonvolume=scale(Mafenetre, from_=100, to=0,fg='yellow', bg='black', variable=Vol)
Buttonvolume.set(50)
Buttonvolume.pack(side = LEFT, padx = 15, pady = 15)

#mode mute
var1 = IntVar ()
tonBouton1 = Checkbutton(Mafenetre, text = "MUTE", command = Mute, variable = var1,fg='yellow', bg='black')
tonButton.pack ()
tonButton.select ()
var1.set (0)

pygame.mixer.music.load(MP3_DIR + '/MIBD.mp3') #musique d'ouverture

#reglage des differents boutons

Play = PhotoImage(file = IMG_DIR + "play.png")
BoutonLecture = Button(Mafenetre, text = 'Lecture', command = Lecture, fg='blue', bg='black', image=play)
BoutonLecture.pack(side=LEFT, padx = 10, pady = 10)

Pause = PhotoImage(file = IMG_DIR + "pause.png")
BoutonPause = Button(Mafenetre, text = 'Pause', command = Pause, fg='blue', bg='black', image=pause)
BoutonPause.pack(side = LEFT, padx = 10, pady = 10)

Reprise = PhotoImage(file = IMG_DIR + "playpause.png")
BoutonUnpause = Button(Mafenetre, text = 'Reprendre lecture', command = Reprise, fg='blue', bg='black', image=reprise) 
BoutonUnpause.pack(side = LEFT, padx = 10, pady = 10)

listbox = Listbox(Mafenetre, width=10)
listbox.insert(0,"PLAYLIST: ")
listbox.pack(side = RIGHT, padx = 10, pady = 10)

#cadre musique

listbox = Listbox (Mafenetre,width=40)
listbox.insert(0, "PLAYLIST: ")
listbox.pack(side = RIGHT, padx = 10, pady = 10)

Mafenetre.mainloop()
