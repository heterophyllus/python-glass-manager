
from zoompan import *
from glass import *
import glob
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def on_show():
    show_plot(combo.current())

def show_plot(plot_type:int=0):
    print("Show button clicked")
    print("Plot type:", combo.get())
    wC = float(entry_wC.get())
    wd = float(entry_wd.get())
    wF = float(entry_wF.get())
    wg = float(entry_wg.get())
    print(wC,wd,wF,wg)

    print("Closing input dialog...")
    app.quit()
    app.destroy()
    
    print("Loading AGF...")
    files = glob.glob("./AGF/*.agf")
    manager = GlassCatalogManager()
    manager.load_agf_files(files)
    manager.set_temperature(25)

    fig = figure()

    #ax = fig.add_subplot(111, xlim=(20,100), ylim=(1.4,2.0), autoscale_on=False)
    ax = fig.add_subplot(111, autoscale_on=True)

    if 0==plot_type:
        ax.invert_xaxis()

    print("Plotting...")
    for catalog in manager.catalogs:
        xlist = []
        ylist = []
        slist = []

        for g in catalog.glasses:
            nC = g.refractive_index(wC)
            nd = g.refractive_index(wd)
            nF = g.refractive_index(wF)
            ng = g.refractive_index(wg)
            PgF = (ng-nF)/(nF-nC)

            if 0==plot_type:
                x = (nd-1)/(nF-nC)
                y = nd
            elif 1==plot_type:
                x = (nd-1)/(nF-nC)
                y = PgF

            s = g.product_name
            xlist.append(x)
            ylist.append(y)
            slist.append(s)

            # text label for each points
            plt.text(x,y,s)
                
            ax.scatter(xlist,ylist, label= catalog.supplier)

    scale = 1.0
    zp = ZoomPan()
    figZoom = zp.zoom_factory(ax, base_scale = scale)
    figPan = zp.pan_factory(ax)

    show()


print("Starting app...")
app = tk.Tk()

label_C = tk.Label(app,text="C [um]: ")
label_C.grid(column=0,row=0)
entry_wC = tk.Entry(app)
entry_wC.grid(column=1, row=0)

label_d = tk.Label(app,text="d [um]: ")
label_d.grid(column=0,row=1)
entry_wd = tk.Entry(app)
entry_wd.grid(column=1, row=1)

label_F = tk.Label(app,text="F [um]: ")
label_F.grid(column=0,row=2)
entry_wF = tk.Entry(app)
entry_wF.grid(column=1, row=2)

label_g = tk.Label(app,text="g [um]: ")
label_g.grid(column=0,row=3)
entry_wg = tk.Entry(app)
entry_wg.grid(column=1, row=3)

combo = ttk.Combobox(app, values=("nd-vd", "PgF-vd"))
combo.grid(column=0,row=4,columnspan=2)
combo.current(0)

button_show = tk.Button(app,text='Show',command=on_show)
button_show.grid(column=0,row=5,columnspan=2)

app.mainloop()
