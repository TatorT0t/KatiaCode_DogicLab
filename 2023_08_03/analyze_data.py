import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bin_analyzed = 3


def plotData(background_y, datax, datay, bin):

    edited_y = datay - background_y
    std_deviation = np.std(edited_y[int(len(edited_y)/14):int(len(edited_y)/5)])


    plt.plot(datax, edited_y, label='Bin'+str(bin)+' edited')
    plt.xlabel('Pixel unit distance')  # Replace with your X-axis label
    plt.ylabel('Pixel intensity')  # Replace with your Y-axis label
    #plt.title('Plot of edited Bin' + str(bin) + ' data')  # Replace with your desired plot title
    plt.grid(True)  # Add grid lines
    plt.legend()  # Show the legend
    #plt.show()

    print()
    print("Data for bin: ", bin)
    print(f"Standard Deviation: {std_deviation:.2f}")

    return edited_y
    

def calcArea(datax, datay, max_index, min_index):
    area_under_curve = 0
    #Stay in loop if data is in range
    x_zone = []
    y_zone = []
    for i in range(len(datax)):
        if datax[i]>min_index:
            #do the riemann sum
            area_under_curve += (datay[i])*(datax[i]-datax[i-1])
            x_zone.append(datax[i])
            y_zone.append(datay[i])
        if datax[i]>max_index:
            break
    return area_under_curve, x_zone, y_zone


#subtract control
def subtract_control(x_data, x_control, y_data, y_control):
    max_data = max(y_data[10:])
    max_control = max(y_control[10:])
    scaling_factor = float(max_data)/float(max_control)

    #DEBUGGING 1:
    y_scaled_control = []
    for i in range(len(y_control)):
        y_scaled_control.append(y_control[i]*scaling_factor*.97)

    #THE SUBTRACTION
    y_extracted = []

    if(len(y_data)>=len(y_scaled_control)):
        for i in range(len(y_scaled_control)):
            y_extracted.append(y_data[i] - y_scaled_control[i])
    else:
        for i in range(len(y_data)):
            y_extracted.append(y_data[i] - y_scaled_control[i])

    '''
    plt.plot(x_data, y_data, label='Original')
    plt.plot(x_data, y_extracted, label='Extracted Data')
    plt.grid(True)  # Add grid lines
    plt.legend()  # Show the legend
    plt.show()
    '''

    return y_extracted, scaling_factor*.97
    


#BACKGROUND ANALYSIS
csv_file_background = 'background_off_gel.csv'
mean_from_file = 1213.299 #this background value (as determined by the square)

data = pd.read_csv(csv_file_background)

x_values_b = data['Distance_(microns)']
y_values_b = data['Gray_Value']

slope_b, intercept_b = np.polyfit(x_values_b, y_values_b, 1)
y_fitted_b = slope_b * x_values_b + mean_from_file

residuals = y_values_b - y_fitted_b
std_deviation = np.std(residuals)


### TEST 3: SUBTRACT BACKGROUND THROUGH A FUNCTION
#plotData(y_fitted_b, x_values_01, y_values_01, bin_analyzed)

#3.1 Bin1:
csv_bin1 = 'bin1.csv'
data_01 = pd.read_csv(csv_bin1)
x_values_1 = data_01['Distance_(microns)']
y_values_1 = data_01['Gray_Value']

y_values_1 = plotData(y_fitted_b, x_values_1, y_values_1, 1)

#3.2 Bin2:
csv_bin2 = 'bin2.csv'
data_02 = pd.read_csv(csv_bin2)
x_values_2 = data_02['Distance_(microns)']
y_values_2 = data_02['Gray_Value']

y_values_2 = plotData(y_fitted_b, x_values_2, y_values_2, 2)

#3.2 Bin3:
csv_bin3 = 'bin3.csv'
data_03 = pd.read_csv(csv_bin3)
x_values_3 = data_03['Distance_(microns)']
y_values_3 = data_03['Gray_Value']

y_values_3 = plotData(y_fitted_b, x_values_3, y_values_3, 3)

#3.2 Bin4:
csv_bin4 = 'bin4.csv'
data_04 = pd.read_csv(csv_bin4)
x_values_4 = data_04['Distance_(microns)']
y_values_4 = data_04['Gray_Value']

y_values_4 = plotData(y_fitted_b, x_values_4, y_values_4, 4)

#3.2 Bin5:
csv_bin5 = 'bin5.csv'
data_05 = pd.read_csv(csv_bin5)
x_values_5 = data_05['Distance_(microns)']
y_values_5 = data_05['Gray_Value']

y_values_5 = plotData(y_fitted_b, x_values_5, y_values_5, 5)

#3.2 Bin6:
csv_bin6 = 'bin6.csv'
data_06 = pd.read_csv(csv_bin6)
x_values_6 = data_06['Distance_(microns)']
y_values_6 = data_06['Gray_Value']

y_values_6 = plotData(y_fitted_b, x_values_6, y_values_6, 6)

#3.2 Bin7:
csv_bin7 = 'bin7.csv'
data_07 = pd.read_csv(csv_bin7)
x_values_7 = data_07['Distance_(microns)']
y_values_7 = data_07['Gray_Value']

y_values_7 = plotData(y_fitted_b, x_values_7, y_values_7, 7)

#3.2 Bin8:
csv_bin8 = 'bin8.csv'
data_08 = pd.read_csv(csv_bin8)
x_values_8 = data_08['Distance_(microns)']
y_values_8 = data_08['Gray_Value']

y_values_8 = plotData(y_fitted_b, x_values_8, y_values_8, 8)

#3.2 Bin9:
csv_bin9 = 'bin9_02.csv'
data_09 = pd.read_csv(csv_bin9)
x_values_9 = data_09['Distance_(microns)']
y_values_9 = data_09['Gray_Value']

y_values_9 = plotData(y_fitted_b, x_values_9, y_values_9, 9)

plt.show()

## TEST4 : DOING THE SUBTRACTION
y_values_4_subtracted, scale_4 = subtract_control(x_values_4, x_values_2, y_values_4, y_values_2)

## Test5 : DO THE RIEMANN SUM

#Controls
area1, x1_subset, y1_subset = calcArea(x_values_1, y_values_1, 50000, 30000)

'''
plt.plot(x_values_1, y_values_1, label='Original Bin1')
plt.plot(x1_subset, y1_subset, label='Extracted Data')
plt.grid(True)  # Add grid lines
plt.legend()  # Show the legend
plt.show()
'''

area2, x2_subset, y2_subset = calcArea(x_values_2, y_values_2, 50000, 30000)
# plt.plot(x_values_2, y_values_2, label='Original Bin2')
# plt.plot(x2_subset, y2_subset, label='Extracted Data')
# plt.grid(True)  # Add grid lines
# plt.legend()  # Show the legend
# plt.show()

area8, x8_subset, y8_subset = calcArea(x_values_8, y_values_8, 50000, 30000)
# plt.plot(x_values_8, y_values_8, label='Original Bin8')
# plt.plot(x8_subset, y8_subset, label='Extracted Data')
# plt.grid(True)  # Add grid lines
# plt.legend()  # Show the legend
# plt.show()


#10kD Data
y_values_3_subtracted, scale_3 = subtract_control(x_values_3, x_values_2, y_values_3, y_values_2)
area3, x3_subset, y3_subset = calcArea(x_values_3, y_values_3_subtracted, 35000, 10000)

# plt.plot(x_values_3, y_values_3, label='Original Bin3')
# plt.plot(x3_subset, y3_subset, label='Extracted Data')
# plt.grid(True)  # Add grid lines
# plt.legend()  # Show the legend
# plt.show()


y_values_6_subtracted, scale_6 = subtract_control(x_values_6, x_values_2, y_values_6, y_values_2)
area6, x6_subset, y6_subset = calcArea(x_values_6, y_values_6_subtracted, 35000, 10000)

# plt.plot(x_values_6, y_values_6, label='Original Bin 6')
# plt.plot(x6_subset, y6_subset, label='Extracted Data')
# plt.grid(True)  # Add grid lines
# plt.legend()  # Show the legend
# plt.show()


#2kD Data
y_values_4_subtracted, scale_4 = subtract_control(x_values_4, x_values_2, y_values_4, y_values_2)
area4, x4_subset, y4_subset = calcArea(x_values_4, y_values_4_subtracted, 42000, 10000)

# plt.plot(x_values_4, y_values_4, label='Original Bin 4')
# plt.plot(x4_subset, y4_subset, label='Extracted Data')
# plt.grid(True)  # Add grid lines
# plt.legend()  # Show the legend
# plt.show()


y_values_5_subtracted, scale_5 = subtract_control(x_values_5, x_values_2, y_values_5, y_values_2)
area5, x5_subset, y5_subset = calcArea(x_values_5, y_values_5_subtracted, 42000, 10000)

# plt.plot(x_values_5, y_values_5, label='Original Bin 5')
# plt.plot(x5_subset, y5_subset, label='Extracted Data')
# plt.grid(True)  # Add grid lines
# plt.legend()  # Show the legend
# plt.show()


#Final answers:

print()
print("Bin 1: ")
print("\t area = ", area1)

print()
print("Bin 2: ")
print("\t area = ", area2)

print()
print("Bin 3: ")
print("\t area = ", area3)
print("\t scaling of control = ", scale_3)
r3 = (area3)/ (area3 + area2*scale_3)
print("\t ratio = ", (area3)/ (area3 + area2*scale_3))

print()
print("Bin 6: ")
print("\t area = ", area6)
print("\t scaling of control = ", scale_6)
r6 = (area6)/ (area6 + area2*scale_6)
print("\t ratio = ", (area6)/ (area6 + area2*scale_6))

print()
print("Bin 4: ")
print("\t area = ", area4)
print("\t scaling of control = ", scale_4)
r4 = (area4)/ (area4 + area2*scale_4)
print("\t ratio = ", (area4)/ (area4 + area2*scale_4))

print()
print("Bin 5: ")
print("\t area = ", area5)
print("\t scaling of control = ", scale_5)
r5 = (area5)/ (area5 + area2*scale_5)
print("\t ratio = ", (area5)/ (area5 + area2*scale_5))

#Final graphs: for bins 3, 4, 5, 6
#Include Original, scaled control, and PEG area

#Bin 3 = 10kD polymerized
y2_scaled = []
y_control = y2_subset #THIS IS PASSED BE REFERENCE. ANY CHANGES DONE TO THIS VARIABLE WILL CHANGE Y_VALUES_2 AS WELL!!
scaling_factor = scale_3
for i in range(len(y_control)):
    y2_scaled.append(y_control[i]*scaling_factor)

plt.plot(x_values_3, y_values_3, label='Original')
plt.plot(x3_subset, y3_subset, label=str('PEG, percent of all tublin: ' + str(r3*100)))
plt.plot(x2_subset, y2_scaled, label='w/o PEG')
plt.grid(True)  # Add grid lines
plt.legend()  # Show the legend
plt.xlabel('Pixel unit distance')  # Replace with your X-axis label
plt.ylabel('Pixel intensity')  # Replace with your Y-axis label
plt.title('Intesity graph of polymerized MT + 10kD PEG')
plt.show()

#Bin 6 = 10kD unpolymerized
y2_scaled = []
y_control = y2_subset #THIS IS PASSED BE REFERENCE. ANY CHANGES DONE TO THIS VARIABLE WILL CHANGE Y_VALUES_2 AS WELL!!
scaling_factor = scale_6
for i in range(len(y_control)):
    y2_scaled.append(y_control[i]*scaling_factor)

plt.plot(x_values_6, y_values_6, label='Original')
plt.plot(x6_subset, y6_subset, label=str('PEG, percent of all tublin: ' + str(r6*100)))
plt.plot(x2_subset, y2_scaled, label='w/o PEG')
plt.grid(True)  # Add grid lines
plt.legend()  # Show the legend
plt.xlabel('Pixel unit distance')  # Replace with your X-axis label
plt.ylabel('Pixel intensity')  # Replace with your Y-axis label
plt.title('Intesity graph of unpolymerized MT + 10kD PEG')
plt.show()


#Bin 4 = 2kD polymerized
y2_scaled = []
y_control = y2_subset #THIS IS PASSED BE REFERENCE. ANY CHANGES DONE TO THIS VARIABLE WILL CHANGE Y_VALUES_2 AS WELL!!
scaling_factor = scale_4
for i in range(len(y_control)):
    y2_scaled.append(y_control[i]*scaling_factor)

plt.plot(x_values_4, y_values_4, label='Original')
plt.plot(x4_subset, y4_subset, label=str('PEG, percent of all tublin: ' + str(r4*100)))
plt.plot(x2_subset, y2_scaled, label='w/o PEG')
plt.grid(True)  # Add grid lines
plt.legend()  # Show the legend
plt.xlabel('Pixel unit distance')  # Replace with your X-axis label
plt.ylabel('Pixel intensity')  # Replace with your Y-axis label
plt.title('Intesity graph of polymerized MT + 2kD PEG')
plt.show()


#Bin 5 = 2kD unpolymerized
y2_scaled = []
y_control = y2_subset #THIS IS PASSED BE REFERENCE. ANY CHANGES DONE TO THIS VARIABLE WILL CHANGE Y_VALUES_2 AS WELL!!
scaling_factor = scale_5
for i in range(len(y_control)):
    y2_scaled.append(y_control[i]*scaling_factor)

plt.plot(x_values_5, y_values_5, label='Original')
plt.plot(x5_subset, y5_subset, label=str('PEG, percent of all tublin:' + str(r5*100)))
plt.plot(x2_subset, y2_scaled, label='w/o PEG')
plt.grid(True)  # Add grid lines
plt.legend()  # Show the legend
plt.xlabel('Pixel unit distance')  # Replace with your X-axis label
plt.ylabel('Pixel intensity')  # Replace with your Y-axis label
plt.title('Intesity graph of unpolymerized MT + 2kD PEG')
plt.show()