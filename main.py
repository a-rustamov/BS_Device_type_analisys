from numpy import count_nonzero
import pandas as pd
import matplotlib.pyplot as plt
import os

def by_device_type (dev_type):
    ''' Take device type and return total, registered and unique device counts per device type  '''
    global total_devices
    global unique_devices
    type_x = df[df['DeviceType'] == dev_type]
    total_devices.append(len(type_x['MacAddress']))
    #registered_devices[count] = 
    unique_devices.append(len(pd.unique(type_x['MacAddress'])))
    #print(type_x.head())
    #print(len(pd.unique(type_x['MacAddress'])))


#Create device dataframe from csv file.
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Data Source', 'Report_User Devices2.csv')
df = pd.read_csv(filename)

#Clean up device type names
df['DeviceType'] = df['DeviceType'].str.replace('-c14811', '')
df['DeviceType'] = df['DeviceType'].str.replace('_c14811_', '-')

#print(df.head())
#print(df.dtypes)

#Create a list of unique device types and itterate over it
device_types = df.DeviceType.unique()
total_devices = []
registered_devices = []
unique_devices = []
for dev_type in device_types:
    by_device_type(dev_type)
print(device_types)
print(total_devices)
print(unique_devices)


