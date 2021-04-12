# -*- coding: utf-8 -*-
import OpenDHW

"""
This Example generates an OpenDHW Timeseries.

Like DHWcalc, OpenDHW need a parametrisation. The usual parametrisation for 
households is 40 L/(person*day). Thus, a 5 person single family house has a mean
drawoff volume of 200 L/day.

A multi family house with 10 flats, and 5 people per flat thus has a mean 
drawoff rate of 2000 L/day.

For non-residental buildings, the daily probability functions should be 
altered, as there are no typical shower or cooking periods in the morning
and the evening.
"""

# --- Parameter Section ---
s_step = 60
people = 5

# --- Plot Parameters ---
start_plot = '2019-03-31'
end_plot = '2019-04-01'

# --- Constants ---
mean_drawoff_vol_per_day_and_person = 40
mean_drawoff_vol_per_day = mean_drawoff_vol_per_day_and_person * people


def main():

    # generate time-series with OpenDHW
    timeseries_df = OpenDHW.generate_dhw_profile_4cats(
        s_step=s_step,
    )

    # Generate Histogram from the loaded timeseries
    OpenDHW.draw_histplot(timeseries_df=timeseries_df)

    pass


if __name__ == '__main__':
    main()