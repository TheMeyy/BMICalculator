import tkinter
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=400,height=400)

def clickButtonCalculator():
    weight = entry.get()
    height = entry2.get()
    if weight == "" or height == "":
        resultLabel.config(text="Lütfen kilo ve boy giriniz!")

    else:
        try:
            BMI = float(weight) / (float(height) / 100) ** 2  # metre cinsinden karesi alınmalı
            if BMI <= 18.5:
                resultLabel.config(text=f"BMI : {BMI} Zayıfsınız")
            elif BMI > 18.5 and BMI <= 24.9:
                resultLabel.config(text=f"BMI: {BMI} Sağlıklı bir kilodasınız")
            elif BMI > 24.9 and BMI <= 29.9:
                resultLabel.config(text=f"BMI: {BMI} Fazla kilolusunuz")
            elif BMI > 30:
                resultLabel.config(text=f"BMI: {BMI} Obezsiniz")
        except:
            resultLabel.config(text ="Numara girmelisiniz")
label = tkinter.Label(text="Enter your weight")
label.pack()
entry = tkinter.Entry(width=25)
entry.pack()
label2 = tkinter.Label(text="Enter your height")
label2.pack()
entry2 =tkinter.Entry(width=25)
entry2.pack()
button =tkinter.Button(text="Calculate",command=clickButtonCalculator)
button.pack()
resultLabel =tkinter.Label() #sonuçlarında ekranda çıkması için
resultLabel.pack()



window.mainloop()