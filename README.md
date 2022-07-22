# BS_Device_type_analisys
![picture 1](../images/7ff62a0dd5df80b87b9ca8679a490b9e8bae403fe308364fd62675b375aa395b.png)  


BS_Device_type_analisys analyzes user/device data from Broadworks phone softswitch. It imports Data/Report_User Devices.csv file containing  device names, types, MAC address and registration. 

## Requirements
* Python 3.9.5 (other 3.3 version should work)
* Import pandas as pd
* Import matplotlib.pyplot as plt


## Setup
* Run *git clone https://github.com/a-rustamov/BS_Device_type_analisys*
* Run *pip install -r requirements.txt* to install the required packages

## Instructions
* From *BS_Device_type_analisys* directory run *python main.py*
  

## Project Requirenments
 1. Import data from local csv *Report_User Devices.csv* 
 2. Cleanup device type names using Pandas replace
 3. * Extract uniqie device type names to *device_types* variable
    * Itterate over *device_types* and call *by_device_type* function
    * Function to find total, unique(based on MAC) and registered number of devices for given device type
 4. Visualize found data using matplotlib. Bar graph with three values. *plot_max_window.py* is used to maximize graph window size for different backgrounds
 5. This readme
 6. Export found data into *Data/Device_type_export.csv*
    



