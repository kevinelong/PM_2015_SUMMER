

# Projection Description

*In my project, I will develop an application to help record the duration of hours worked by individuals.
This application will then email a summary of hours worked by each individual to an email of the user's choosing.

_Components_

---
## New user registration
---

*User will see login screen requesting employee/time sheet number but underneath a link will be displayed highlighted in blue “New User Registration”
Once user is registered, approval would be needed by admin(myself or individual owner), a email notification sent to admin requesting access.


---
# User Time Stamp
---

*User will see a box requesting employee/time sheet number and a box to the right reading “Time Stamp”.
This will send information of time and date to the database of when individual clocks in and out of the work day.

---
#Time records
---

*This will be a secondary button underneath the “Time Stamp” button, reading “Recorded Time” which will then pop up a new window with previous recorded time stamp marks(clock in, clock out, lunches, breaks). (user inputs employee/time sheet number in same field)

---
#Email response
---

*Will not be seen by common users. (Set up through admin.)

*Email requirements will be in place to validate address given. Used to send customized info sent to super user.

---
Time Line
---

1.  Models: Make models for data base to save into
2.  User Registration: Create form requesting company affiliation, first name and last name.
3.  User Time Stamp: Create event listeners and handlers for accompany given character fields. Used to record time stamps. Test with improvised users and assign each employee/time sheet numbers.
4.Views and Templates: Craft login page, Time stamp page.
5.Information format: Find way to format information received from application, to be ready for email.
6.Email: Figure out a way to use Django or some service to send requested information.
7.Styling: Put more CSS, Javascript into project to make it look more interactive and look more appealing to the eyes

---
#Later project improvement
---

*Make it to where program randomly generates employee/time sheet ID number
*Give application mobile functionality
*Give authorization automatically without secondary approval through admin with use of randomly generated code given by admin prior to logging in