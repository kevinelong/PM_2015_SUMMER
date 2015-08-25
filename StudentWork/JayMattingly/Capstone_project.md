# Projection Description

In my project, I will develop an application to help record the duration of hours worked by individuals.
This application will then email a summary of hours worked by each individual to an email of the user's choosing.

# Components

## New user registration

The user will see a login screen requesting the employee/time sheet number.The user will also see underneath, a link will be displayed highlighted in the color blue “New User Registration”.

Once the user is registered, an approval from the administrator would be needed. An email would be formatted with this information, sent to the administrator.(myself or individual owner), a email notification sent to admin requesting access.

## User Time Stamp

The user will see a box requesting an employee/time sheet number and a box to the right labeled “Time Stamp”.

Once the user clicks the “Time Stamp” button, their input, time and date will be sent to a database populating the individual's daily work hours recorded.

## Time records

There will be a secondary button underneath the “Time Stamp” button, reading “Recorded Time” which will then pop up a new window with previous recorded time stamp marks(clock in, clock out, lunches, breaks). (user inputs employee/time sheet number in same feild)

## Email response

Will not be seen by common users. This will be set up through the administrator.

Email requirements will be in place to validate address given. Used to send customized info sent to super user.


# Time Line

1.  Models: Create models.py file and decide what fields to have for application
2.  User Registration: Create a forms.py file requesting company affilation, first name and last name.
3.  User Time Stamp: Create an event listener for “Time Stamp” button in javascript for handling . Used to record time stamps. I will test fields with improvised users and assign each employee/time sheet numbers.
4.  Views and Templates: Craft login page, Time stamp page and their corresponding urls required to find pages with in application.
5.  Information format: Research the method I will use to send all required information in an email format.
6.  Styling: Pretty up my template pages with CSS and implement Javascript into my application to make it look more interactive and look more appealing to the eyes.

# Later project improvement

  * Make it to where program randomly generates employee/time sheet ID number
  * Give application mobile functionality
  * Give authorization automatically without secondary approval through admin with use of randomly generated code given by admin prior to logging in
