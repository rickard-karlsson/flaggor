# Kodad i Python 3.5.1 med PyCharm 5.0.4
# Rickard Karlsson 2016-08-03

# Detta program är ett bildspel med några länders flaggor och lite info om dem.

import sys
import tkinter
from PIL import Image, ImageTk

# Globala variabler
currentimage = 0 # Index för vilken bild som ska visas
piclist = [] # Lista för bilderna som används
textlist = [] # Lista för bildtexterna
textbox = None # Ruta för bildtexterna
canva = None # Ruta för bilderna
root = tkinter.Tk() # Jag har provat sätta denna som None och använda som global i setGUI, men får en hel massa
                    # felmeddelanden om att bilderna inte laddas. Hjälp?


def load_images():  # Läser in alla bilder som ska användas
    global piclist

    try:
        piclist = [
            ImageTk.PhotoImage(Image.open("Denmark.png")),
            ImageTk.PhotoImage(Image.open("Norway.png")),
            ImageTk.PhotoImage(Image.open("Finland.png")),
            ImageTk.PhotoImage(Image.open("Poland.png")),
            ImageTk.PhotoImage(Image.open("Russia.png")),
            ImageTk.PhotoImage(Image.open("Estonia.png")),
            ImageTk.PhotoImage(Image.open("Latvia.png")),
            ImageTk.PhotoImage(Image.open("Lithuania.png"))
        ]
    except:
        print("Något gick fel vid inläsning av bilder.")
        avsluta()


def create_texts(): # Skapar bildtexterna i en lista
    global textlist

    textlist = [
        "Danmarks flagga \"dannebrogen\" är världens äldsta, från tidigt\n1200-tal. \n\nSverge har varit i krig mot Danmark 13 gånger.",
        "Norges flagga antogs 1821 och färgerna är kombinerade från de\nsvenska och danska flaggorna.\n\nI Norge kan man köpa elbilar momsfritt.",
        "Finlands flagga antogs efter finska inbördeskriget 1918. Färgerna\nrepresenterar snö och vatten.\n\nDet finska ordet 'kalsarikännit' "
        "betyder att sitta hemma och supa\ni underkäder, utan avsikt att gå ut.",
        "Polens färger har länge varit rött och vitt, men nuvarande\nflaggan antogs 1918.\n\nPolacker hävdar att dom uppfann vodka.",
        "Rysslands flagga antogs 1991 efter Sovjet föll, men har funnits\nsen 1690-talet.\n\nRyssar hävdar att dom uppann vodka.",
        "Estlands flagga antogs 1990 efter befrielsen från Sovjet, men har\nanor sedan 1881.\n\nEstlands president föddes i Sverige"
        " och växte upp i USA.",
        "Lettlands flagga antogs 1990 men är mycket äldre än det.\n\nUnder sovjettiden tillverkades i Riga mindre transportbussar"
        " till\nhela Sovjetunionen.",
        "Litauens flagga skapades 1918 men antogs senast 1989. \n\nLitauen har ett av världens bästa landslag i basket.",
    ]

def insert_text(x): # Sätter in text i textrutan
    global textbox
    global textlist
    textbox.delete(1.0, tkinter.END)
    textbox.insert(0.0, textlist[x])


def insert_image(y): # Sätter in en bild i bildrutan
    global canva
    global piclist
    canva.delete("all")
    canva.create_image(0, 0, image=piclist[y], anchor='nw')


def next_image(): # Visa nästa bild
    global currentimage
    if currentimage < 7: # Gå framåt endast om man inte är vid sista bilden
        currentimage += 1
        insert_image(currentimage)
        insert_text(currentimage)


def prev_image(): # Visa föregående bild
    global currentimage
    if currentimage > 0: # Backa bara om man inte är vid första bilden
        currentimage -= 1
        insert_image(currentimage)
        insert_text(currentimage)


def avsluta(): # Avsluta programmet
    sys.exit(0)


def setGUI():
    global canva
    global root
    global textbox
    global textlist

    #root = tkinter.Tk() #Om jag sätter denna här istället förstör det mitt program.

    root.title("Några av Sveriges grannländer.")

    topframe = tkinter.Frame(root) # Övre ramen för bild och bildtext
    topframe.pack(side="top")

    lowerframe = tkinter.Frame(root) # Den undre ramen för knapparna
    lowerframe.pack(side="bottom")

    canva = tkinter.Canvas(topframe, width=480, height=350, bg="lightgrey") # Ruta för bilder
    canva.pack(side="top")
    canva.create_image(0, 0, image=piclist[currentimage], anchor='nw') # Visa första bilden

    textbox = tkinter.Text(topframe, width=65, height=6, bg="white") # Textruta för bildtexterna
    textbox.pack(side="bottom")
    textbox.insert(0.0, textlist[0]) # Visa första bildtexten

    previous = tkinter.Button(lowerframe, text="Föregående", command=prev_image) # "Föregående"-knappen
    previous.pack(side="left")

    nextpic = tkinter.Button(lowerframe, text="Nästa", command=next_image) # "Nästa"-knappen
    nextpic.pack(side="left")

    avslutaknapp = tkinter.Button(lowerframe, text="Avsluta", command=avsluta) # "Avsluta"-knappen
    avslutaknapp.pack(side="left")


def main():
    load_images()
    create_texts()
    setGUI()
    root.mainloop()


if __name__ == '__main__':
    main()