 common approximation for calculating battery storage revenue is the TBn method. TBn revenue is defined as the sum of top “n” priced hours at any point in the day minus the sum of bottom “n” priced hours at any point in the day.
The benefit of this method is that it captures the simple economic approach of a battery: buying low and selling high. It also replicates some of the core constraints, namely the limited amount of battery energy.

    1. Write a function to calculate TBn revenue which takes an input price dataframe with two columns( date, price) and an integer ‘n’.
    2. Calculate the daily TB2 revenue at HB_NORTH for DAM & RTM separately using the csv file from task_1. Save the output in two csv files named as ‘dam_tb2.csv’ &             ‘rtm_tb2.csv’ containing two columns: date in ‘yyyy-mm-dd’ format and tb2 value rounded up to 2 decimal digits.
