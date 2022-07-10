import pandas as pd
import matplotlib.pyplot as plt
import os
from plot_max_window import plt_maximize


def by_device_type (dev_type):
    ''' Take device type and update total, registered and unique device counts per device type    '''
    type_x = df[df['DeviceType'] == dev_type]
    total_devices.append(len(type_x['MacAddress']))
    registered_devices.append(len(type_x[type_x['Registered'] == True]))
    unique_devices.append(len(pd.unique(type_x['MacAddress'])))
    #print(type_x.head())
    #print(len(pd.unique(type_x['MacAddress'])))


def export_device_type(dev_type, total_devices, registered_devices, unique_devices):
    '''Export to CSV total devices, registered devices and unique devices per device type'''
    df_export = pd.DataFrame.append(total_devices, columns=dev_type)

#Create device dataframe from csv file.
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Data', 'Report_User Devices.csv')
df = pd.read_csv(filename)

#Clean up device type names
df['DeviceType'] = df['DeviceType'].str.replace('-c14811', '')
df['DeviceType'] = df['DeviceType'].str.replace('_c14811_', '-')

#Create a list of unique device types and itterate over it to record total, registered and unique devices
device_types = df.DeviceType.unique()
total_devices = []
registered_devices = []
unique_devices = []
for dev_type in device_types:
    by_device_type(dev_type)

#Make dictionary out of found data, create dataframe
dict_for_df = {'Device Type': device_types,
               'Total': total_devices, 'Registered': registered_devices, 'Unique': unique_devices}
#df_export = pd.DataFrame(dict_for_df).set_index('DeviceType')
df_export = pd.DataFrame(dict_for_df)

#Export dataframw to CSV
export_filename = os.path.join(dirname, 'Data', 'Device_type_export.csv')
df_export.to_csv(export_filename)

# Plot resulted data
plt.rcParams.update({'font.size': 6})  # must set in top
df_export = df_export.sort_values(by='Total', ascending=False) #Set descending order based on total devices
df_export.plot(x='Device Type', y=[
               'Total', 'Registered', 'Unique'], kind='bar', figsize=(14, 20))
plt.subplots_adjust(bottom=0.22)
plt.xlabel("Device Type")
plt_maximize()
plt.show()



