from tkinter import *
import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def initialize():
    # *** Button Label *** #
    label1 = Label(frame, text='Percentage of Urban Population',fg='Black', bg='#8DB600')
    label1.config(font=('Times New Roman', 18))
    label1.place(x=165, y=100)

    label2 = Label(frame, text='Input', fg='Black', bg='#8DB600')
    label2.config(font=('Times New Roman', 15))
    label2.place(x=85, y=245)

    label3 = Label(frame, text='Predicted Output', fg='Black', bg='#8DB600')
    label3.config(font=('Times New Roman', 15))
    label3.place(x=85, y=425)

    # *** Button 1 *** #
    button1 = Button(frame, text='Predict', fg='Black', bg='silver', width=5, command=prediction)
    button1.config(font=('Times New Roman', 13))
    button1.place(x=200, y=345)

    # *** Button 2 *** #
    button2 = Button(frame, text='Plot', fg='black', bg='silver', width=5, command=plotData)
    button2.config(font=('Times New Roman', 13))
    button2.place(x=300, y=345)

    # *** Button 3 *** #
    button3 = Button(frame, text='Solve', fg='black', bg='silver', width=5, command=solved_line)
    button3.config(font=('Times New Roman', 13))
    button3.place(x=400, y=345)


def solved_line():
    # Create linear regression object
    regr = LinearRegression()
    regr.fit(x_parameter, y_parameter)
    plt.scatter(x_parameter, y_parameter, color='#8DB600', marker='+', label='Data')
    plt.plot(x_parameter, regr.predict(x_parameter), color='cyan', linewidth=1, label='Line')
    plt.legend(loc='best')
    plt.title('Year vs Percentage of Urban Population')
    plt.xlabel('Year')
    plt.ylabel('Percentage of Urban Population')
    plt.show()


def plotData():
    plt.scatter(x_parameter, y_parameter, c='#8DB600', marker='+', label='Data')
    plt.legend(loc='best')
    plt.title('Year vs Percentage of Urban Population')
    plt.xlabel('Year')
    plt.ylabel('Percentage of Urban Population')
    plt.show()


def prediction():
    # Create linear regression object
    regr = LinearRegression()

    # Get Predict value from textfield
    predict_value = float(input1.get("1.0", "end-1c"))

    # Train Data
    regr.fit(x_parameter, y_parameter)

    # Predict Value
    predict_outcome = regr.predict(predict_value)

    show_output = float(predict_outcome)




    lbl = Label(frame, text=show_output, bg='silver', fg='black')
    lbl.config(font=('Times New Roman', 15))
    lbl.place(x=235, y=425)


if __name__ == '__main__':
    # Declare Frame #
    root = Tk()
    frame = Frame(root, width=650, height=500, bg='#8DB600')
    frame.pack()

    # Text Field #
    input1 = Text(frame, height=1, width=15,bg='silver', fg='black')
    input1.config(font=('Times New Roman', 15))
    input1.place(x=195, y=245)

    # Extract Data from csv file #
    file_name = 'C:\\Users\\uwaze\\Desktop\\Population.csv'
    data = pd.read_csv(file_name)
    x_parameter = []
    y_parameter = []
    for Year, Population_Density in zip(data['Year'], data['Population']):
        x_parameter.append([float(Year)])
        y_parameter.append(float(Population_Density))

    print(type(x_parameter))
    print(type(y_parameter))

    initialize()

root.mainloop()
