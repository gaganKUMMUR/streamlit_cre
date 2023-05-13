import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

st.title("Chemical reaction Engineering")
st.header("Method to find the order of Reaction of the given concentration by Linear Fitting")
st.write("This website is dedicated to the collection and analysis of data. Our primary focus lies in employing numerical methods to calculate the rate of reactions, enabling us to estimate both the rate constant and the order of reaction.")
t = [0,1,2,3,4]
n = st.number_input('Insert number of reading',5,10)
for i in range(5,int((n+1))):
    t.append(i)
# f = [15,12,11,7,6]
a=[]
b=[]
coefficients=[]
slp=1
ipt=1
def rate_calculator(n,b,a):
  c=(-3*f[0]+4*f[1]-f[2])/2
  b.append(c)
  for i in range((n-1)):
    c=(f[i+2]-f[i])/2
    b.append(c)
  b.append((f[n-2]-4*f[n-1]+3*f[n])/2)
  print (b)
  for i in range (n+1):
      b[i]=math.log(-b[i])
  plot_data(t,f, "concetration vs time", 'concetration in mol/m^3')
  return

def fit_line_equation(x, y):
    # Fit a line to the data
    coefficients = np.polyfit(x, y, 1)
    slope = coefficients[0]
    intercept = coefficients[1]
    slp=slope
    ipt=intercept
    # Construct the equation of the line
    equation = f"y = {slope:.2f}x + {intercept:.2f}"
    print (equation)
    return coefficients

def plot_data(x, y,name,yaxis, xaxis='time in sec'):
    # Plot the data points
    
    fig, ax = plt.subplots() 
    ax.scatter(x, y, color='blue')

    ax.set_xlabel(xaxis)
    # ax.set_xlim(xmin=0)
    ax.set_ylabel(yaxis)
    # ax.set_ylim(ymin=0)
    ax.set_title(name)
    ax.grid(True)
    for i, txt in enumerate(y):
        ax.annotate("%0.2f" %(txt), (x[i], y[i]))
    st.pyplot(fig)
    
def plot_line(slope, intercept):
    # Define x values
    x = np.linspace(-10, 10, 100)

    # Calculate y values
    y = slope * x + intercept

    # Plot the line
    fig, ax = plt.subplots() 
    ax.plot(x, y, color='blue',label='y=%fx+%f' %(slope,intercept))
    ax.set_xlabel('x')
    # ax.set_xlim(xmin=0)
    ax.set_ylabel('y')
    # ax.set_ylim(ymin=0)
    ax.set_title('line fitted through linear regression')
    ax.grid(True)
    ax.legend(loc="upper left")
    st.pyplot(fig)



# print ("initial concentration")
# ca0=float(input())
ca0 = st.number_input('initial concentration',15.00)
a.append(ca0)
d = [st.number_input(f'enter concentration after {str(i+1)} miniutes', value=ca0-i-2, max_value=ca0,key=f"text_input_{i}") for i in range(n)]
g=[0,0,0,0,0,0]
m= []
if len(d) !=0:
   f = a+d

for i in range(n+1):
   m.append(math.log(f[i]))

if len(m) ==0:
   m = g

print ("a", f)
print("g",m)
rate_calculator(n,b,a)
plot_data(m,b, "-ln(d(ca)/dt) vs ln(ca)", xaxis='ln(ca)',yaxis= '-ln(d(ca)/dt)')



coefficients = fit_line_equation(m,b)
plot_line(coefficients[0],coefficients[1])
st.write("Order of the reaction is : %f" %(coefficients[0]))
print ("order of the reaction is:")
print (coefficients[0])
print ("rate constant of the raction is:")
print (pow(2.71,coefficients[1])/60)
st.write("Rate constant of the reaction is : %f in SI units" %(pow(2.71,coefficients[1])/60))
st.write("_______________________________________________________________________________________________________")

st.write("Gagankumar c kummur 2021BB10348")
st.write("Paramesh palo 2021CH10414")
st.write("Bhukya Tarun 2021BB10370")
