# Budgeting App

## 1.0 UX

### 1.1 User Goals

#### 1.1.1 Target Audience

### 1.2 User needs and how they are met

#### 1.2.1 User needs

#### 1.2.2 How the user needs are met

### 1.3 Developer goals

### 1.4 User Stories

## 2.0 Design Choices

### 2.1 Fonts

### 2.2 Icons

### 2.3 Colours

### 2.4 Wireframes

### 2.5 Mockups

## 3.0 Features

### 3.1 Exisiting features

### 3.2 Features left to implement

## 4.0 Technologies used

### 4.1 HTML5

### 4.2 CSS3

### 4.3 Bootstrap

### 4.4 JavaScript

### 4.5 jQuery

### 4.6 Python

### 4.7 Flask

### 4.8 MongoDB

## 5.0 Testing

## 6.0 Development life cycle 

### 6.1 Initial commit

Added:

- README.md file

### 6.2 Flask setup

Added:

- app.py file
- env.py file
- Installed Flask
- Added README template

### 6.3 requirements.txt

Added:

- requirements.txt

### 6.4 Added Procfile

Added:

- Procfile

### 6.5 Deployed to heroku

Added:

- Updated requirements.txt

### 6.6 Project connected to mongodb

Added:

- Templates folder
- base.html
- index.html
- MongoDB via URI

### 6.7 Static files added and frontend setup

Added:

- Static folders
- style.css
- script.js
- Bootstrap added
- jQuery added
- Font awesome added

### 6.8 Nav and footer v0.0.1

v0.0.1 Additions:

- Navbar responsive on all devices
- Footer responsive on all devices

### 6.9 Users can securely create an account v0.1.0

v0.1.0 Additions:

- login.html file
- signup.html file
- Werrkzeug secrurity added
- Sign up functionality

### 6.10 Log in functionality and flash messages v0.2.0

v0.2.0 Additions:

- Log in functionality
- Added flash messages to base template

### 6.11 Users can log out of their account v0.2.1

v0.2.1 Additions:

- Users can log out of their account

### 6.12 Nav and footer links added v0.2.2

v0.2.2 Additions:

- Log in and sign up links show when users aren't logged in
- Log out and other links show only when users are logged in
- Footer links

### 6.13 add_record page v0.2.3

v0.2.3 Additions:

- add_record.html added
- Add record template

### 6.14 Successfuly posted record to mongodb v0.3.0

v0.3.0 Additions:

- Successfuly posted record to mongoDB

### 6.15 Basic summary page structure and test file v0.3.1

v0.3.1 Additions:

- Summary page basic structure
- summary.html
- testing.md
- Displays users records

Bug #1 found: Summary link throws error 404 when clicked on from home page

### 6.16 Account page and set balance POST's v0.3.2

v0.3.2 Additions:

- Account page
- Set account balance
- Balance POST's to mongoDB

### 6.17 Users can update their account balance v0.3.3

v0.3.3 Additions:

- Users can update their account balance

### 6.18 Adding records changes the accounts balance v0.3.4

v0.3.4 Additions:

- testing.md updates
- Income records add the amount to the new balance
- Other records subtract the amount from the old balance
- Updates the user's total balance

### 6.19 Category tracker created upon user sign up v0.3.5

v0.3.5 Additions:

- When users sign up it creates a categories document on MongoDB to keep track of spending
- Updates categories with new values

Issue: Resets categories everytime record is added fix will come in next version

### 6.20 Category tracker updates after adding record and sign up page set account balance v0.3.6

v0.3.6 Additions:

- When a record is added the category tracker updates with the new category total and grand total
- v0.3.5 Issue resloved category no longer resets upon adding records
- Sign up page set account balance so users don't have to go to profile page first

### 6.21 Category tracker on summary page and paycheck basic structure setup v0.3.7

v0.3.7 Additions:

- Summary page displays category tracker and totals them up
- Created paycheck.html
- Set up paycheck page links and basic structure

### 6.22 Successful post from paycheck page v0.4.0

v0.4.0 Additions:

- Set paycheck income
- Created paycheck collection on MongoDB
- Successfully posted to MongoDB paycheck collection

### 6.23 Auto caclulates total paycheck v0.4.1

v0.4.1 Additions:

- Auto caclulates total paycheck
- Created test.html

### 6.24 Removal of paycheck feature v0.4.2

v0.4.2 Additions:

- Removal of test.html
- Removal of test function
- Removal of paycheck.html
- Removal of paycheck function
- Removal of paycheck JS

### 6.25 Removal of category tracker, updated add record v0.5.0

v0.5.0 Additions:

- Removal of categories feature temporaily
- Add record working
- Add record page basic css
- home page basic css

## 7.0 Deployment

### 7.1 Heroku Deployment

### 7.2 Local Deployment

## 8.0 Credits

### 8.1 Content

### 8.2 Code
