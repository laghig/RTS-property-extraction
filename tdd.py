# -*- coding: utf-8 -*-
import sys
import numpy as np
import pandas as pd
import datetime as datetime

def interpolate_temp(pd_data):
    """
    Interpolate by previous values
    Note: 
        - better interpolate by nearest value??
    """
    nans = pd_data['Mean Temp (°C)'].isnull()
    for j in range(len(pd_data['Mean Temp (°C)'])):
        # if first nan set to -999

        if j == 0:
            if nans[j]:
                pd_data.loc[j, 'Mean Temp (°C)'] = -999
                continue

        if nans[j]:
            if pd_data.loc[j-1, 'Mean Temp (°C)'] <= 0:
                pd_data.loc[j, 'Mean Temp (°C)'] = -999
            else:
                pd_data.loc[j, 'Mean Temp (°C)'] = 999  

    return pd_data

def get_tdd(date1, date2, pd_data):

    """
    computes the number of thawing degree days between date1 and date2 based on the data in pd_data
    Input:
        date1 (datetime object): early date
        date2 (datetime object): second date
        pd_data(panda dataframe): needs entries 'Date/Time' and 'Mean Temp (°C)'

    Output:
        number of tdd's
    """

    tdds = 0
    for date, temp in zip(pd_data['Date/Time'], pd_data['Mean Temp (°C)']):

        date_ = datetime.datetime.strptime(date, '%Y-%m-%d')

        if date1 <= date_ <= date2:

            if temp > 0:

                tdds += temp

    return tdds

if __name__ == '__main__':


    # define csv_file location

    csv_file = [r"D:\Meteo_Data\en_climate_daily_NU_2401200_2009_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2010_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2011_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2012_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2013_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2014_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2015_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401200_2016_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401203_2016_P1D.csv",
        r"D:\Meteo_Data\en_climate_daily_NU_2401203_2017_P1D.csv"]

    csv_data = []

    for csv_file_ in csv_file:

        csv_data.append(pd.read_csv(csv_file_))


    data = pd.concat(csv_data, axis=0, ignore_index=True)


    # if some database points are missing they need to be interpolated

    # data = interpolate_temp(data) old version - interpolate by previous value

    data['Mean Temp (°C)'] = data['Mean Temp (°C)'].interpolate(method='nearest') # inpolate by nearest value

    # data['Mean Temp (°C)'] = data['Mean Temp (°C)'].interpolate(method='polynomial', order=3) # other options...

    # Manually define the start and end date in which tdd should be calculated
    date1 = datetime.datetime(year=2012,month=8,day=27)
    date2 = datetime.datetime(year=2013,month=8,day=1)

    tdds = get_tdd(date1, date2, data.copy())
    print(tdds)