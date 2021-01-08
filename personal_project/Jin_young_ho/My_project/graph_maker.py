#GUI
import tkinter as tk
import tkinter.ttk as ttk

#graph
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()

root.title('graph_maker')
root.geometry('500x500')
root.resizable(False, False)

def graphmake():
    #graph_data
    data = {'X': [], 'Y': []}

    #error part, edit_x1, edit_x2, edit_y1, edit_y2 print '\n'
    data['X'] = [int(edit_x1), int(edit_x2)]
    data['Y'] = [int(edit_y1), int(edit_y2)]

    
    #graph
    df2 = DataFrame(data,columns=['X', 'Y'])

    figure2 = plt.Figure(figsize=(5,4),dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['X', 'Y']].groupby('Y').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color = 'r', marker = 'o', fontsize  = 10)
    ax2.set_title('this is graph')

x = tk.Label(root, text="X축", font = 16)
x.place_configure(x=1, y=1)

x_data1 = tk.Text(root, width = 5, height = 1.3 )
x_data2 = tk.Text(root, width = 5, height = 1.3 )
x_data3 = tk.Text(root, width = 5, height = 1.3 )
x_data4 = tk.Text(root, width = 5, height = 1.3 )
x_data5 = tk.Text(root, width = 5, height = 1.3 )
x_data6 = tk.Text(root, width = 5, height = 1.3 )
x_data7 = tk.Text(root, width = 5, height = 1.3 )
x_data8 = tk.Text(root, width = 5, height = 1.3 )
x_data9 = tk.Text(root, width = 5, height = 1.3 )
x_data10 = tk.Text(root, width = 5, height = 1.3 )

x_data1.place(x =40, y = 3)
x_data2.place(x = 80, y = 3)
x_data3.place(x = 120, y = 3)
x_data4.place(x = 160, y = 3)
x_data5.place(x = 200, y = 3)
x_data6.place(x = 240, y = 3)
x_data7.place(x = 280, y = 3)
x_data8.place(x = 320, y = 3)
x_data9.place(x = 360, y = 3)
x_data10.place(x = 400, y =3)


y = tk.Label(root, text="y축", font = 16)
y.place_configure(x=1, y=50)

y_data1 = tk.Text(root, width = 5, height = 1.3 )
y_data2 = tk.Text(root, width = 5, height = 1.3 )
y_data3 = tk.Text(root, width = 5, height = 1.3 )
y_data4 = tk.Text(root, width = 5, height = 1.3 )
y_data5 = tk.Text(root, width = 5, height = 1.3 )
y_data6 = tk.Text(root, width = 5, height = 1.3 )
y_data7 = tk.Text(root, width = 5, height = 1.3 )
y_data8 = tk.Text(root, width = 5, height = 1.3 )
y_data9 = tk.Text(root, width = 5, height = 1.3 )
y_data10 = tk.Text(root, width = 5, height = 1.3 )

y_data1.place(x =40, y = 50)
y_data2.place(x = 80, y = 50)
y_data3.place(x = 120, y = 50)
y_data4.place(x = 160, y = 50)
y_data5.place(x = 200, y = 50)
y_data6.place(x = 240, y = 50)
y_data7.place(x = 280, y = 50)
y_data8.place(x = 320, y = 50)
y_data9.place(x = 360, y = 50)
y_data10.place(x = 400, y = 50)

edit_x1 = x_data1.get("1.0", "10000.0")
edit_x2 = x_data2.get("1.0", "10000.0")
edit_x3 = x_data3.get("1.0", "10000.0")
edit_x4 = x_data4.get("1.0", "10000.0")
edit_x5 = x_data5.get("1.0", "10000.0")
edit_x6 = x_data6.get("1.0", "10000.0")
edit_x7 = x_data7.get("1.0", "10000.0")
edit_x8 = x_data8.get("1.0", "10000.0")
edit_x9 = x_data9.get("1.0", "10000.0")
edit_x10 = x_data10.get("1.0", "10000.0")

edit_y1 = y_data1.get("1.0", "10000.0")
edit_y2 = y_data2.get("1.0", "10000.0")
edit_y3 = y_data3.get("1.0", "10000.0")
edit_y4 = y_data4.get("1.0", "10000.0")
edit_y5 = y_data5.get("1.0", "10000.0")
edit_y6 = y_data6.get("1.0", "10000.0")
edit_y7 = y_data7.get("1.0",  "10000.0")
edit_y8 = y_data8.get("1.0", "10000.0")
edit_y9 = y_data9.get("1.0", "10000.0")
edit_y10 = y_data10.get("1.0", "10000.0")


button = tk.Button(root, 
              text="생성하기",
              command=graphmake)
button.place_configure(x=220, y=100)

root.mainloop()
