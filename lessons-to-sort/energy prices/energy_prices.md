Energy prices can be broken into two components - blocks and scalars. Energy block is the average energy price for a set of hours and energy scalar is a list of hourly factors that denotes the shape.


Hours from 06:00 to 21:00 (16 hours) are considered as peak hours and remaining 8 hours are considered as off-peak hours. Thus, average energy price of peak hours for one day would give you the peak energy block for that day.


Energy scalars can be calculated as hourly energy price divided by the respective block price. The unique property of scalars is that the average of scalars at block level should always be 1.


You need to calculate energy blocks and energy scalars at monthly level for both peak and off-peak block using the input prices from hourly_prices.csv

Attached is the hourly_prices.csv

Deadline 1800 hrs
