# Capstone Project Proposal: WoohooList

WoohooList is a social media app where users create communities that help them achieve their goals. Users create profiles in which they choose a large goal (such as running a marathon) and break it down into smaller steps, then "friend" others who have goals in the same broad category. They are rewarded both for accomplishing their goals and for encouraging others through a point system.

## Components

## Login and new user signup

Registered users can sign in from the WoohooList homepage. They will be able to see their own profile page as well as a feed of their friends' accomplishments. Logged in users will also see their points and their "next step" wherever they are on the page.

## Goal setting page/user profile

On the goal setting page/profile, there is a form where users set goals. Users designate a specific, achievable large goal (e.g. "Run my first 5K") and a timeline (e.g. "In 3 months"). They then break the goal into smaller steps that will be repeated daily or several times a week (e.g. "Train 3 times a week"). The finished page will have the large goal at the top as well as an overview of their plan and how much of it they've accomplished (measured by the point system).

## Friending other users and accomplishments feed

Each goal will have a category (fitness, finance, etc.) and each profile page will automatically display links to the profiles of others with similar goals. Then they can click on an icon on their profile to "friend" them and see their accomplishments listed on a feed. Each user will see their feed when they log in.

## Comments and point system

When users click on a friend's accomplishment, they will be taken to a detail page with a comment form. They will also be able to see others' comments. Leaving a comment will increment the count of their total points on their user profile. 

## Timeline

1. Develop Goal App
- Map out models and make migrations
- Make view for goal setting page (read only to users at this stage)
- Make base template with CSS themes
- Create template for goal setting page (all templates from now on extend base)
- Create form that will allow user to choose/edit goal and create steps

2. Develop Account App
- Map out models and make migrations for User class
- Make view for profile page
- Make template for profile page

3. Add user login capability
- Make view for login page
- Make template for login page
- Make authentication form

4. Add functionality to Account App
- Devise point system
- Display user's current points on profile page
- Devise search function to query for users with similar goals
- Adjust template of profile page so it links to profiles of people with similar goals
- Add button on profile page that will allow others to friend a user

5. Add Functionality to Goal App
- Make view and template for "feed" page that will show friends' recent accomplishments
- Add Comment class to existing models and make migrations
- Make view and template for detail page for each "step" toward goal
- Add form that will allow users to leave comments on a certain step

6. Finishing Touches
- Add more JavaScript (such as animations or alerts congratulating you when you accomplish something)
- Make custom templates for error pages

## Ideas for Later

* Users can add multiple big goals and designate one as primary goal
* More nuanced searching for other users' goals
* Users can make goals visible only to friends
* Users can block specific other users and report inappropriate content
* Logging in through Facebook or Google