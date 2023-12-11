# User Manual

Team 6: Sports League Track System

## Version 1.0

This goal of project is to build a database to keep track of sports league, we use flask framework and MongoDB and simple GUI for user esay to use.

## Graphical User Interface

The Sports League Track system Graphical User Interface is a revolutionary user friendly interface to interact with the Sports League Database System.

You can create your own account and create your own database, therefore, we offer the register and login and edit account function. We want to protect you safety of the information.

<img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h8lobjaquej30gy08wweq.jpg" alt="Screenshot 2022-11-28 at 10.08.14" style="zoom: 33%;" />

When you successful login, you can come into our main system menu. Then you can choose what you want. And create your own tracking for the sports.

<img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h8lobo6ujqj30eo042gln.jpg" alt="Image 11-27-22 at 12.48" style="zoom: 50%;" />

### Add 

From the menu bar select `Add`. This will bring up the `Add Menu`. Then click which you want to add.

<img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h8lobreqv6j30c409gq39.jpg" alt="Image 11-27-22 at 12.50" style="zoom:33%;" />



* Add a new league

  You should input the following information, then click submit.

  `League name `, `Commissioner` , `SSN` 

  The three things cannot input null or repeat as the data in the database.

* Add a new team

  You should input the following information, then click submit.

  `Team name` `State` `City` `Field Count` `Rating` `League Name`

  Field count can be null, and the rating is number. If you do not set the rating, it will set default as 0. Others can not be null.

* Add a season 

  You should input the following information, then click submit.

  `League name` `Season name` `Begin date` `End date` `Season state` `Season city` `Team field/Count`

* Add a new game

  * Manual adding

    You should input the following information, then click submit.

    `League name` `Season name` `Team1 name` `Team2 name` `Game date` 

  * Generating random games

    You should input the following information, then click submit.

    `League name ` `Season name`

* Add result

  `League name ` `Season name` `Team A` `Team B ` `Team A score` `Team B score` `Game date`

Your data will be imported into the database. The system will output any errors found in the data. Most of type of data have some limits. If not follow the limits, the system will not add the data into the system.

### Query

From the menu bar select `Query` . This will bring up the `Query Menu`. Then click which you want to query.

<img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h8lobsuwdjj30cu0buaal.jpg" alt="Image 11-27-22 at 12.51 (1)" style="zoom: 50%;" />

* League basic query

  You should input the following information, then click query.

  `League name`

  Then the basic information *league name, commissioner, seasons* about the league will be displayed

* League more detail query

  You should input the following information, then click query.

  `League name`

  Then the basic informaiton *league name,  commissioner* about the league and more detail about the seasons, like *seasons name, champions, rating* and *game records* will be displayed.

* Team basic query

  You should input the following information, then click query.

  `Team name`

  Then the basic informaiton *team name ,city, field* about the team will be displayed.

* Team more detail query

  You should input the following information, then click query.

  `Team name`

  Then the basic informaiton *team name, city, field* about the team and more detail about the seasons, like *seasons name, rating* and *game records* will be displayed.

* Game query

  You should input the following information, then click query.

  `Team1 name` `Team2 name` 

  Then the informaiton *team name, results* about the teams will be displayed.

* Season query 

  You should input the following information, then click query.

  `League name` `Season`

  Then the informaiton *League name, Season name,  results* about the seasons will be displayed.

* Rating query

  You should input the following information, then click query.

  `League name` `Team name`

  Then the rating will displayed on the system.

You need to put the information to tell the system what you want , you can not click query something with null input. And the system will output some hints about the errors found in the data. Also the system will tell you which part you might wrong. You can try it again. We want to offer you right information.

### Modify

From the menu bar select `Modify`. This will bring up the `Modify Menu`. Then click which you want to modify.

<img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h8lobw520kj30c405uq34.jpg" alt="Image 11-27-22 at 12.52" style="zoom:33%;" />

* Update the current date

  You should input the following information, then click query. 

  `update the date`

  Then the system will display whether you successful update the current date. If wrong it will tell you. The default time will depend on your system local time. 

* Move team

  You should input the following information, then click query.
  
  `Team name` ` Future league name`

### Delete

From the menu bar select `Delete`. This will bring up the `Delete Menu`. Then click which you want to delete. We just give user for two things to delete. If you want to more function about that, please follow the future versions. 

* Delete team

  `Team name`

  Then the system will delete the information about the team, but we will not delete the records in the pass.

* Delete a league

  `League name`

  Then the system will delete the information about the league, but we will not delete the teams records of the pass.
  
  
  

This system just the first version, if you want to have more functions, please follow the future versions. 

  

​	



