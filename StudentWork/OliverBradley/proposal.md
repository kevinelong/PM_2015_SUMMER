# Capstone Proposal

## Project Description

My project is to create a forex charting platform.  The user will be able to input a forex pair (i.e. EUR/USD), a date range and a time frame (i.e. 15 minutes) and return a chart representing the data.


## Components

### Login and new user sign up

A new user will be able to sign up, create a new user name and password and get a URL created specific to him or her.

### Pair information page

The user will be able to access information about a particular pair he or she is interested in and view information including:

	* base currency rate
	* trading hours
	* dates in database
	* minimum tick size
	* tick value

### Chart

The user will be able to view a chart of his or her specification (date range and time frame).  The URL should reflect these specifications:

	http://base_URL/USERNAME/PAIR/START_DATE/END_DATE/TIME_VALUE/TIME_NUMBER

	i.e.

	http://forex.com/dadsaster/EUR_USD/01_01_2015/01_15_2015/HOUR/1

This will be built in D3.js which requires data to be provided as json.

### Database Update

I will use the Oanda.com API to populate and keep the database up to date.  When a returning user logs in the application should check to see if the database is behind current time and update itself accordingly.

## Timeline

    **Models**: Map out all models and create all migrations.
    **API interactions**: Write all code for getting data from API and populating the database
    **Templates and views**: Create the pages for charts and user.
    #. **Users and authentication**: Write login page, figure out how to allow interested people how to request an account.
    **Polish and style**: 404 and 500 error pages, CSS, JavaScript to make the page look great.

## Ideas for Later

    * add point and figure charting
	* add streaming data and updates for current bar
	* add volume histogram
	* add basic trend line creationht.

