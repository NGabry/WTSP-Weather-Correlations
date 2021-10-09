# Performing correlations using White-thraoted Sparrow hatch date data and weather variables 
DESCRIPTION OF PROJECT

## Long-term Weather Trends 

SPEARMAN_TREND.py - ONLY USED FOR WEATHER TRENDS
	
Always type 'python spearman_trend.py' first

For overall trends from 1900 to 2020, enter 1 argument

For specific monthly trends from 1900 to 2020, enter 2 arguments

	argument 1 = one of the below weather variables,
	
	argument 2 = any month's Digit (i.e. If Jan enter 1, Feb enter 2, etc.)

EXAMPLE: To run correlation on TAVG in January, type 'python spearman_trend.py TAVG 1'

'''{python} spearman_trend.py TAVG 1'''

## Correlations with Hatch Date 

CORRELATE.py and PREVIOUS_CORRELATE.py - USED FOR REGRESSING JULIAN DATE VARIABLES ON WEATHER

For correlate.py, previous_correlate.py

Always type 'python *SCRIPT_NAME*.py' first

3 arguments are required

	argument 1 = any month's Digit (i.e. If Jan enter 1, Feb enter 2, etc.)
	
	argument 2 = JULIAN or EARLIEST, WxT_AVG, TxW_AVG, WxT_EARLIEST, TxW_EARLIEST

	argument 3 = one of the below weather variables 

EXAMPLE: To run correlation on JULIAN with TAVG in January, type 'python correlate.py 1 JULIAN TAVG' or 'python previous_correlate.py 1 JULIAN TAVG' for January of the previous year. 

'''{python} correlate.py 1 JULIAN TAVG'''

'''{python} previous_correlate.py 1 JULIAN TAVG'''

## WEATHER VARIABLES

* TAVG = Mean Monthly Temperature °C
* TMAX = Mean Maximum Temperature °C
* TMIN = Mean Minimum Temperature °C
* HTDD = Heating Degree Days (# of degrees below 18° C across the month)
* CDD = Cooling Degree Days (# of degrees below 18° C across the month)
* ABSMAX = Absolute Maximum Temperature recorded
* ABSMAX_DATE = Date ABSMAX occured
* ABSMIN = Absolute Minimum Temperature recorded 
* ABSMIN_DATE = Date ABSMIN occured
* ABS_RANGE = ABSMAX minus ABSMIN
* DX32 = # of Days with Max temp >= 32° C
* DX0 = # of Days with Max temp <= 0° C
* DT0 = # of Days with Min temp <= 0° C
* DT-18 = # of Days with Min temp <= -18° C
* PRCP = Total precipitation in mm
* PRCPMAX = Maximum daily preciptation in mm
* PRCPMAX_DATE = Date PRCPMAX occured
* SNOW = Total snowfall in mm
* SNOWMAX = Maxmim daily snowfall in mm
* SNOWMAX_DATE = Date SNOWMAX occured
* DP.25 = Days with precipitation >= .25 mm
* DP2.5 = Days with precipitation >= 2.5 mm 
* DP25X = Days with precipitation >= 25 mm 
