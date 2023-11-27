import numpy as np

# Calculate the area of each grid
area = ds['solar_mon'].sel(lat=slice(-90, 90), lon=slice(0, 360)).mean(dim='time') * 0 + 1
area = area * np.cos(np.deg2rad(ds['solar_mon']['lat']))
area = area * np.deg2rad(ds['solar_mon']['lon'] - ds['solar_mon']['lon'][0])
area = area * 6371.009 ** 2 * 1e6

# Calculate the total incoming solar radiation
total_solar = ds['solar_mon'].sel(lat=slice(-90, 90), lon=slice(0, 360)).mean(dim='time') * area
total_solar = total_solar.sum(dim=['lat', 'lon'])

# Calculate the total outgoing longwave radiation
total_lw = ds['toa_lw_all_mon'].sel(lat=slice(-90, 90), lon=slice(0, 360)).mean(dim='time') * area
total_lw = total_lw.sum(dim=['lat', 'lon'])

# Calculate the total outgoing shortwave radiation
total_sw = ds['toa_sw_all_mon'].sel(lat=slice(-90, 90), lon=slice(0, 360)).mean(dim='time') * area
total_sw = total_sw.sum(dim=['lat', 'lon'])

# Print the results
print('Total incoming solar radiation:', total_solar.values, 'W/m^2')
print('Total outgoing longwave radiation:', total_lw.values, 'W/m^2')
print('Total outgoing shortwave radiation:', total_sw.values, 'W/m^2')