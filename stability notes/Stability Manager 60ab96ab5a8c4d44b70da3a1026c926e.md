# Stability Manager

Created: May 16, 2022 8:15 AM

# Day 1

# Sample Management

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled.png)

### Results

- Tests contain Results.
- Can be manually entered
or updated via form.
- Manually Entered
    - From Requests Tab Test
    Side bar: Enter results
    - From Tests Tab side bar:
    Enter Results
    -

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%201.png)


### Test

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%202.png)

- Test Definition must include:

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%203.png)

    - Unique Test ID
    - Department (Stability)
    - One Mandatory Results
    - Note: Number of Units (Stability) (NEW)
        - each time you run a sample, it will take away from that inventory.

### Sample Templates

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%204.png)

- Number of samples is required instability
- should be added to methods

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%205.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%206.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%207.png)

- Grouping of tests associated with a study
- Typically grouped based on test intervals
    - E.g. qualitative, quantitate, and microbiology tests
    Defined within LMS
    Main Menu -> Administration -> Sample Templates
- Sample Template must include:
    - Sample Template Name
    - Field Configuration
    - Location
    - Number of Samples

### Specifications

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%208.png)

- Specification for stability

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%209.png)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2010.png)

    - if you create a second formulation for stability spec, then you cant create another spec under the first formulation
    - spec example

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2011.png)

    - Specifications define all tests run on a
    product and formulation.
    Defined within LMS
    Main Menu -> Administration -> Specifications
- Must Include:
    - Unique Specification ID
    - Product
    - Formulation
    - Category
    - Field Configuration
    - Available for stability module (checked)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2012.png)

- Can Add predefined Tests/ Methods/ Sample Templates.
- Specification needs to be approved.
- Product category

    Defines how many signatures are
    required for:

    - Release of a request.
    - Release of a request with an Out of
    Specification (OS) result.
    Define a default report template to
    use

    ![Our system has Finished requre a signature to released](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2013.png)

    Our system has Finished requre a signature to released

- Important notes

    Sample Templates and Tests can be made at the specification level (not
    methods.)
    Acceptance Criteria specified on the Specification level overrides any Sample
    Template/Method/Test level criteria.

    ![cant go back and change approved specs](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2014.png)

    cant go back and change approved specs


### Requests

Request Ties Samples to Tests
Contains Various Metadata:
Product Name

- Formulation
- Category
- Storage Condition
- Department

### Submission

Submissions Automatically Created by Stability

- Contains Samples to be tested
- Includes Stability Batch
Identifier as well as specific timepoint being tested.
Each Sample also generates a corresponding request(s) according to the Sample Template.
- Submissions are Automatically Managed User does not need to modify submission status.

### Basic Workflow

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2015.png)

- Notes
    - Stability Module generates Submission, Request and Tests
    - Tests are created based on the defined sample template
    - Submission is not considered completed until the request has been released.

## Training

### Went to this link and typed in our code

[https://waters.instructorled.training](https://waters.instructorled.training/)

4537748601 - Edie

4537748602 - Mat

4537748603 - Christine

4537748604 - Hung nguyen

4537748605 - Samra

- click on Lab, then click on connect box then type in the login
    - Account: NuGenesis RPC
    - Password: Manager1

### Steps

- Passwords in Passwords.txt
- NuGenesis Training Information:

    User:
    demoadmin
    demouser

    Password:
    Goodluck1
    Goodluck1
    NuGenesis Oracle Container SID: NG91
    LMS Oracle SID: SDMS
    WDM login:
    user:
    password:
    administrator
    administraton

- open LMS
- Create product and Formulation named Stability *
    - Stability will not use Formulation composition
- Create a Method
    - GSN 221 Vitamin C
- Create a test under the method

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2016.png)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2017.png)

    - click Save and Approve method

### Go to Specification Tab

- Click new specification

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2018.png)

- Click Add new sample template

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2019.png)


### Note to Admins

- typically we dont have groupings in our Sample templates page
    - show Sample template Header and Group On Sample Template
    - This will separate the two

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2020.png)

## Admin Configuration Options

- Sample management
    - Fields
        - All columns are Metadata, we can configure who can see what on each tab
- External system


    if ever having trouble connecting to stability module check here

    Transfer modifiable versions of sample templates and specifications checkbox

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2021.png)

    - recommends leaving it unchecked because otherwise there is a lot of noise  every-time you change a spec
    - LWR: Lab Work Requests
    - Department for stability submissions
        - Determines who can see the stability samples
    - Users to be notified
        - sends any errors or issues stability is having to their inbox
        - recommends adding Admins and some stability people
    - Activate background jobs
        - adds two new jobs to

            ![In Dev its 60 seconds, in PRD it should be longer (600 sec)](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2022.png)

            In Dev its 60 seconds, in PRD it should be longer (600 sec)

        - Submissions Create Request
            - Automatically create requests for any submissions that come in
            - Controlled under Admin > Submission Templates tab

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2023.png)

                - The Skip Reception box is checked for stability  but not QC (angela manually checks the samples before)
- User Managment

    Dont want the LMS admin account to be synced over to Stability

    - Samra and Christine will be part of this group (and mat And Edie)
    - Make sure Privileges is set correct

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2024.png)

    - Stability has its own Permission to configure

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2025.png)


# Day 2

## Intro to Stability

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2026.png)

- Stability UI

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2027.png)

- Shortcuts bar

    ![Enter Some wont be used because it will be handled by LMS](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2028.png)

    Enter Some wont be used because it will be handled by LMS

    - LWR example:


        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2029.png)


- Structure of Stability Study

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2030.png)

    Notice there are several study folders on each level.

    - clicking on the studies shows you all the studies inside the directorys below

    - Organization for VitaQuest will be Vitaquest


        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2031.png)

    - Daniel will follow up with how we should organize by customer or not
- Structure of Stability Study -LWR

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2032.png)

    - it will apply the sample template

## Initial Configuration

## Stability Specific Master Data within LMS

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2033.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2034.png)

- can also restrict users based on product

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2035.png)


## Nugenesis Lists

- SM Product Family List

    Just used for metadata, it is not nessasary

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2036.png)

- SM_Organization

    will dictate the organizations in Stability


## Managing Stability Users

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2037.png)

-
- Security (see Table provided)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2038.png)

    - Master Data - Products with formulation


        -

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2039.png)


    ## Admin tools

    can set Change control codes for quick select

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2040.png)

    - Can view deleted items in teh Deleted items folder
    - Ingredients: the list of ingredients for the formulations

# Training

### Open Stability Manager

 add new ingredient

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2041.png)

things like Labs, and Manufacture sites have to be added through LMS lists

- Spec Alerts: will record the Spec alerts that get generated from LMS
- Storage conditions Holds all the conditions for your chambers

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2042.png)

    - can set the positions of the conditions (have to reload the folder after)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2043.png)

    - Orientation:

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2044.png)

    - Creating inverted versions by right click> copy

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2045.png)



### Storage Location

 can add Chambers and storange locations to the tree

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2046.png)

have to enable inventory to make lower levels to inventory

- Go to Right click > Properties > details to choose the conditions for the chambers and Locations

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2047.png)

-

### Studies

- can show studies in this view, but it is limited to only viewing 500

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2048.png)

-



### Suppliers

-

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2049.png)

- can add abatches to the ingredients and the configure the supliers and stuff
-

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2050.png)

### Master Tag List

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2051.png)

- Creates options for you in drop downs. (like Batch/lot Uses > Current use)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2052.png)

- or Ingredient Type in Vitamin C Properties
    -

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2053.png)

- NonPull Events
    - add a tag for nonpull Events
- Packaging types: Bottles, vials, box etc

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2054.png)

- Product families, result qualifiers, and specification status all managed by LMS
- Storage Category:

    Protical matrix for storage condition

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2055.png)

- Storage Orientation

    Study purposes define the details tab o


###

-
-

### LMS ADMIN

### Open lists

create a new list SM Result Conforms > New Value > Conforms & Does Not Conform

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2056.png)

### Create a new Spec template

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2057.png)

### Add New sample templates to the spec

analytical physical, and Micro

- Add Vitamin C to analytical template

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2058.png)

    - Add Appearance test( dont forget to make Number of units 1)
        -

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2059.png)


### IMPORTANT: Stability cant have 0 0 limits in micro

it works in LMS but not Stability, so just leave upper 0

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2060.png)

### Open up stability>Clients> Milford>stability product, stability Formulation

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2061.png)

this is the one we made

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2062.png)

- Sample templates

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2063.png)

    - Stability and LMS have their own versions codes (Internal Revision Code/External Version Code)
        - one starts at 0, the other starts at 1
        - another example is snake oils
            - because the _____

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2064.png)


### Create a study

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2065.png)

- fill out info

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2066.png)

### Select Storage conditions and intervels

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2067.png)

### Matrix stability Protocol Editor

- drag the sample templates into the Cell

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2068.png)

- another way of adding could be from right click

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2069.png)

- can add nonpull events
-

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2070.png)


### Add New Formulation Component

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2071.png)

### Units Needed comes from LMS

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2072.png)

we set the units to 1 in the LMS specs

- this comes form the Protocol matrix, where each test is a unit
-

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2073.png)

### add storage conditions properties

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2074.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2075.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2076.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2077.png)

- Scheduling the study

### Approve the study

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2078.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2079.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2080.png)

??

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2081.png)

### Display testing schedules shortcut

![Through list is how much in advance do you want it to show the staility info](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2082.png)

Through list is how much in advance do you want it to show the staility info

### calendar view

- could right click and request Study/LWR

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2083.png)

- could also right click and undo the requst on the LDR
- Could also do multiple Pulls (click and drag)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2084.png)


### WorkLoad Balance

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2085.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2086.png)

- Pull The requests from the Stability Tree (the batch)

    ![or click the PULL LIST shortcut](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2087.png)

    or click the PULL LIST shortcut

    then select the 3 and then right click > Pull

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2088.png)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2089.png)

    now they are set to Pulled

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2090.png)


### Check Submissions in LMS

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2091.png)

### Questions about Requests vs Pulls

- Request is setting what you want in what day(setting it to stone), A Pull creates a submission in LMS. Requests is always a step that is needed.
- The system will auto request them a day before they are pulled though
- A request can be done a few days before the pull
- [x]  Daniel will follow up on if you can increase the range it will auto request, to like a week or month before the day.
    - it cannot. Best to just do a mass reuest with a mass pull

# Day 3

### Enter results to pending test

- Click ‘show sample’ on the in pending test in the Submissions tab
- Enter results for the tests

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2092.png)

### you can see the study name and timepoint column show a link to the LWR

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2093.png)

- can have the option to display comments on the report
- Finish Report
- go back to submissions tab, hit refresh, and it should show completed,
- go back to stabiity and refresh F5

![the last two steps are done by LMS](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2094.png)

the last two steps are done by LMS

### Recap of day 1 and 2

### you can edit tests under node

- if the test is ‘under revision’

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2095.png)

- you can remove vitamin C and it will show an * to show its not the original study

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2096.png)

-

### Printing to PDF

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2097.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2098.png)

### you can view results in matrix

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%2099.png)

(approve does not work)

- the Regulatory checkbox when doing stability report, you have the option to not report a study
-

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20100.png)

### Pull Request

- right click on the request and go to pull

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20101.png)

-

![this window pops up every time, you can close it](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20102.png)

this window pops up every time, you can close it

-

### Go back to LMS and see the submissions

- there are 2 submissions becaouse of the timepoint

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20103.png)

- then enter the all the results and complete the tests
- go back to stability to see that they are approved

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20104.png)

### click view results on the batch

- make sure both the bottom checkboxes are show

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20105.png)

### click on study and go to launch report generator

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20106.png)

-

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20107.png)

### Customize the report by clicking on the magnifying glass in Report Generator

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20108.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20109.png)

- a lot of these fields (metadata) from the Stability manager will show up on the report
- the certificate of analysis >cant show multiple conditions/timepoint (might not be useful to us)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20110.png)


### how to update specifications

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20111.png)

- then go to sample templates

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20112.png)

- (only the original sample templates)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20113.png)

- so you have to Copy Sample Template to update it. Then it will show the Rev. #

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20114.png)

### the point of New Variants (like EU)

- Varients just wont flag samples as OOS in LMS if they are out of range

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20115.png)

    - click on New Varient and then a new column shows up where you can enter other spec ranges

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20116.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20117.png)

        - then in the Report generator you will be able to switch the Spec to the varient

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20118.png)

        -
    -
    -

### Favorites

- you can save certain studies under the favorites folder to find faster.

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20119.png)


### For non-pull events, just right click and go to complete

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20120.png)

### Status for studies

- you have all these sstatus for the study

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20121.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20122.png)

### Various reports

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20123.png)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20124.png)

### Statistics Module

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20125.png)

- select condition(s)

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20126.png)

- The sub Vit C is the Result, that is the one you pick

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20127.png)


![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20128.png)

- you choose various options and how results are treated under the Statistics Menu
    - the scaling sucks

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20129.png)

- Saving
    - some theings wont be avilable till you save it
    - create a new folder and save it there

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20130.png)


## You have the ability to change around the records

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20131.png)

-

# Questions\notes

- can you show e-signatures or logo
    - no e-signatures
    - To add Logo, go to Page setup, and you can add a logo and header

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20132.png)

- separating stability samples in LMS

    ![Here is where you control the department to use stability](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20133.png)

    Here is where you control the department to use stability

    ![we would remove test operations but have admin to see it](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20134.png)

    we would remove test operations but have admin to see it

    - go

### how do you request/pull more than on at at time

on the calander view you can drab and drop

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20135.png)

- you get there by clicking on the Calander icon

![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20136.png)

- Make sure batches are ‘under revision’ to edit them. (right click and go to Properties)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20137.png)

- 2 different conditions and two different intervals
    - change around these conditisons

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20138.png)

    - will show up here

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20139.png)

    - you would specify if its accelerated, intermediate, or longterm

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20140.png)

    -
- Structure clients based on company
    - another option is to utilize the ProductFamily list and select them in the Products Tab
    - then you will be able to see it here

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20141.png)

    -
- what happens when there is two products (canada and US) but share the same stability study(same batch # too)


- Adding Unique identifier for the study
    - it wont be out of the box because it wont fit in the header of the report
        - we can use study fields or notes or info, and it

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20142.png)

    - Wants a uniue id for typing it into a search bar

- We wont be able to hide the (n) after the Method name

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20143.png)

- you can copy the Pull Lists and add it to Excel

    it might be easier to filter in stability manager first

- does the system notify you if you miss a sample
    - no, you can set it up notification for only missed Pulls,
    - there is a way to set up a jasperreport and have that send user messages if a sample is missed.
- how to include tests on the label,

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20144.png)

    you can edit a label template in LMS, but you have to be good at XML.

- Can enable Customer name to show, but you have to do it manually each time. (or set up a template for each customer)

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20145.png)


- Example K277, K571
    - [ ]  Are we going to have to create new methods for every stability test since the Department has to be stability?
    - [ ]  do we have to do a result unit for every possibile combo?

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20146.png)

    - [ ]  Is there anything you would like me to add or switch over?
    - [ ]  Who is adding any New specs for Stability?
    - [ ]  Is there a list to address?
    - [ ]  Should i switch the Intertek methods?
        - [ ]  What happens when you lock a method? does it effect current ones?
        - [ ]

        ---



    - Methods

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20147.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20148.png)

    - Spec templates

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20149.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20150.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20151.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20152.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20153.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20154.png)

    - Sample Template
        - Under the sample template there is a location tied to it. Each location is tied to a department.
        - You would need to
            1. Create the Stability department
            2. Go to Locations and add the new location that is associated with the Stability department
                1. Administration Page → Sample Management Category – Locations

                    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20155.png)

            3. Create a new version of your specification
            4. Update the sample templates locations you want with the new location created in step 2.

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20156.png)

            5. Approve specification

        When this syncs to stability the LWRs that use these latest sample templates will now appear under this department.

    -
- Trouble shooting with stability
    - E: \WatersLMSServer\log -> Manager.log

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20157.png)

        - When a test is deleted instead of canceled, the Stability gives error.
            - Daniel is looking to see if he can prevent that
    - Gives error if you dont log an initial date in inventory K324

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20158.png)


    ![because there date isnt set. you have to go to properties an set it](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20159.png)

    because there date isnt set. you have to go to properties an set it

    - Show calander view/list of what is scheduled
        - can click on the Calender to show upcoming batches scheduled

        ![you can manually change it to show](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20160.png)

        you can manually change it to show

    - Cant change the order of tests

        no, that would have to be a features

- character limit on Result id?
    - max character is 64 char

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20161.png)

- Change NLT > < NMT signs
    - cant do it individually without changing test spec

    ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20162.png)

    - To have an Esignature you will have to go through SDMS
- Is it worth creating a Custom CoA to generate through LMS?
    - Since they said all the information is available in the same database, we would be able to retrieve it the same way it gets retrieved on our current Vitaquest CoA.
    - I think all i would need is help with where to find the data from Stability Module. (which is what Kevin was talking about with the SQL Schema). if they can help with that we can build the rest of the JaspeReport to work like the current Vitaquest CoA.
    - It would be able to be e-signed then, and also custom order of the tests.

    - SDMS
        - print the Report generate

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20163.png)

        ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20164.png)

        - THen user goes onto vision and login

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20165.png)

            Brous project, and find the project from stability

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20166.png)

            - you can click on the report and SDMS will load the file
            -

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20167.png)

            then sign in

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20168.png)

            then authenticate

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20169.png)

            then you have hte option to place a signature

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20170.png)

            - then print it out to pdf
            - tehn it adds the Signature history and the image
            -

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20171.png)

            you cant change the image of the signature

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20172.png)

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20173.png)

            SDMS collects the metadata and can use it to sort or export elsewhere if needed

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20174.png)

            ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20175.png)

            - edge doesnt work with Vision, only internet explorer


                Use this website to loginto Vision

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20176.png)

                you have to add it to trusted sites for it to work in internet explorere

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20177.png)

                then

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20178.png)

                then

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20179.png)

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20180.png)

                then install certificate on local machine

                ![Untitled](Stability%20Manager%2060ab96ab5a8c4d44b70da3a1026c926e/Untitled%20181.png)

                then place all certificate in the in the “Personal Folder”


[Day 4](https://www.notion.so/Day-4-b76798ca6f47405192f1822c1d148624)