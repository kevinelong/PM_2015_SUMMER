Sample Capstone Proposal
------------------------

*In this sample proposal, I will be using my Audition Magician idea. Use this
document as a guild while creating your own. Text that is in italics are
comments on each section of the proposal. Non-italic text is my actual proposal
text.*


Project Description
===================

*In this section you will describe what the project is. Explain in one or two
sentences exactly what your project will do.*

My project is to create an Audition Magician website. Users can sign up to
receive emails for when orchestras will be offering auditions for their
instrument.


Components
==========
*This is the section where you will describe each of the parts of your site.
Each of these sections needs to have at least 2-3 sentences of description of
what it is and the experience of using it from the user end.*

Login and new user sign up
``````````````````````````
A registered user can click in the upper right hand corner to log in. Once
logged in, they can have access to details on their account. This includes
adding and removing which orchestras they are interested in.

Because my Audition Magician website will be in beta once deployed, I want to
be able to approve all new users. If someone wants to have a new user account,
I will provide a link for them to contact me. This will either be an email or
filling out a form.

User detail page
````````````````
This page will be viewable by logged in users. A user can update any of their
information. They can add/remove any orchestras they are interested in. There
will also be a link to be able to suggest a new orchestra.

Orchestra list
``````````````
This page will show the current list of all orchestras in the database.
Registered and non-registered users can suggest new orchestras to add to the
list. Each orchestra name will link to its detail page.

Orchestra detail
````````````````
This page will give all details about the orchestra. This will include if there
is currently an audition available. A logged in user can request to add the
orchestra to those they want to receive reports about. Anyone can suggest an
edit or a new audition. This suggestion will need approval from a moderator.

Finding new auditions
`````````````````````
This is the meat of the website. Once a night, a management command will be run
that will scrape the audition web listings for each orchestra. If a new
audition is found, an email will be sent to the users that have requested
updates.

This section could be very buggy because it is relying on a webscraper. For
that reason, the website will remain in beta (new user registrations closed)
until all kinks are worked out.


Timeline
========
*In this section you will describe the order that you will complete each of the
above components. As you do this, imagine yourself in class having just
completed a task and consider what you will need to do next.*

    #. **Models**: Map out all models and create all migrations.
    #. **Audition finder**: Write the management command that will do the
           webscraping.
    #. **Templates and views**: Create the pages for orchestra list, orchestra
           detail, user detail.
    #. **Users an authentication**: Write login page, figure out how to allow
           interested people how to request an account.
    #. **Polish and style**: 404 and 500 error pages, CSS, JavaScript to make
           the page look great.


Ideas for Later
===============

*It is important not to kill the creative process by ignoring great ideas.
However, because you will have a limited amount of time for your capstone, some
of these ideas have to be out of scope. Here is where you will list these.*

    + Support searching for auditions for any instrument
    + Login with Google or Facebook
    + A new user can confirm an email change
