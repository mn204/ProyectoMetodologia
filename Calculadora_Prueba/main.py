import tkinter as tk
import math

calculation = ""

def addCalculation(symbol):

    
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#La funcion evaluar tiene problemas de seguridad, podrian introducir codigo 3ros
def evaluateCalculation(): 
    
    global calculation
    print(calculation) 

    try:
        
        result= str(eval(calculation))
        calculation=""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clearField()
        text_result.insert(1.0, "end")
        pass

def squareRoot():
    global calculation
    try:
        result = str(math.sqrt(float(calculation)))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except Exception as e:
        clearField()
        text_result.insert(1.0, "Error")
        pass

def clearField():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")
    pass


root = tk.Tk()
root.geometry("375x275")

text_result = tk.Text(root, height=1, width=19, font=("Arial", 24))#16 originalmente
text_result.grid(columnspan=6)#5 columnas originalmente
root.title("Calculadora")

btn_7 = tk.Button(root, text="7", command=lambda: addCalculation(7), width=5, font="Arial, 14")
btn_7.grid(row=2, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: addCalculation(8), width=5, font="Arial, 14")
btn_8.grid(row=2, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: addCalculation(9), width=5, font="Arial, 14")
btn_9.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: addCalculation(4), width=5, font="Arial, 14")
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: addCalculation(5), width=5, font="Arial, 14")
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: addCalculation(6), width=5, font="Arial, 14")
btn_6.grid(row=3, column=3)

btn_1 = tk.Button(root, text="1", command=lambda: addCalculation(1), width=5, font="Arial, 14")
btn_1.grid(row=4, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: addCalculation(2), width=5, font="Arial, 14")
btn_2.grid(row=4, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: addCalculation(3), width=5, font="Arial, 14")
btn_3.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: addCalculation(0), width=5, font="Arial, 14")
btn_0.grid(row=5, column=1)

btn_00 = tk.Button(root, text="00", command=lambda: addCalculation(00), width=5, font="Arial, 14")
btn_00.grid(row=5, column=2)

btn_dot = tk.Button(root, text=".", command=lambda: addCalculation("."), width=5, font="Arial, 14")
btn_dot.grid(row=5, column=3)#puede dar error de operdaro por el . en vez de ,

btn_plus = tk.Button(root, text="+", command=lambda: addCalculation("+"), width=5, font="Arial, 14")
btn_plus.grid(row=4, column=4, rowspan=2, sticky="ns")
#   El parámetro sticky se utiliza en Tkinter para indicar cómo debe 
#   expandirse o ajustarse un widget dentro de su celda de la 
#   cuadrícula. Podria usar los 3 nsew
#    n: El widget se pega a la parte superior de la celda.
#    s: El widget se pega a la parte inferior de la celda.
#    e: El widget se pega al lado derecho de la celda.
#    w: El widget se pega al lado izquierdo de la celda.

btn_X = tk.Button(root, text="x", command=lambda: addCalculation("*"), width=5, font="Arial, 14")
btn_X.grid(row=3, column=4)

btn_percent = tk.Button(root, text="%", command=lambda: addCalculation("%"), width=5, font="Arial, 14")
btn_percent.grid(row=2, column=4)

btn_equal= tk.Button(root, text="=", command=evaluateCalculation, width=5, font="Arial, 14")
btn_equal.grid(row=5, column=5)

btn_minus= tk.Button(root, text="-", command=lambda: addCalculation("-"), width=5, font="Arial, 14")
btn_minus.grid(row=4, column=5)

btn_div= tk.Button(root, text="\u00F7", command=lambda: addCalculation("/"), width=5, font="Arial, 14")#unicodes
btn_div.grid(row=3, column=5)

btn_sqrt = tk.Button(root, text="√", command=squareRoot, width=5, font="Arial, 14")
btn_sqrt.grid(row=2, column=5)


root.mainloop()
