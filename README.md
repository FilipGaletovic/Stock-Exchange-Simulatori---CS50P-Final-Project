Stock Exchange Simulator

Video Demo: <URL https://youtu.be/PJcbXocgjJE>

Description:
A simple stock trading simulation that lets users register, log in, check their balance, and trade a selection of NASDAQ stocks. User data, including balance and transactions, is stored in a JSON file to save progress between sessions.


Features User Authentication Login:

Users are prompted for their username and password to log in. If no users are registered yet, the login attempt will fail, and the user will be prompted to register. Register:

Users can create a new account with a unique username and secure password. When creating a new user, a new instance of the class account is created, following the username, password and balance variables that have their property and setter methods. Username requirements: Must be unique (no duplicates). Password requirements: Must include at least one uppercase letter, one number, and one special character. The password is stored in a hash 256 format for a more secure system, using the hashlib library. After registering, each new user starts with a $10,000 balance. User data, including hashed passwords and initial balances, is saved in accounts.json. That data from accounts.json file is later on fetched from load_save.py file. The two functions used are load_users and save_users. Load_users function takes the file name as a parameter and returns the list of users. Save_users function takes the filename and new users data dictionary and dumps it into the json file. Exit: Users can exit the app directly from the authentication menu.

Main Menu After logging in or registering, users will access the main menu, with the following options:

Display Balance: Shows the user’s current available balance and any invested balances. Invested balance is updated depending on the hour you run the program because it's fetching real time data and stock prices, making your investment lose or gain in value.

Search for Stocks: Users can search stocks by entering the stock symbol (e.g., AAPL). The user can search up to 50 NASDAQ stocks which are stored in the get_stock_info.py file, as a dictionary. The function get_stock checks if the given stock exists in the stock dictionary, if so using the request library, json element containing the stocks information is returned. After searching, the user is shown the latest stock price information and prompted to buy shares if none are currently owned. If the user already owns shares, they can either buy more or sell shares. Any purchases or sales automatically update the user's balance and are saved to the JSON file.

Exit and Save: Saves all user data (balances, investments) and exits the app.

All of the functions are error caught with either try-except blocks or if elif checks to make the experience more user friendly

The app will not quit until save and exit option is selected.

Imports: ->os ->sys ->hashlib ->re

Libraries: ->json (standard library) ->Any additional libraries will need to be added here if necessary

API: ->Alpha Vantage - https://www.alphavantage.co/documentation/ This API is used to fetch data about stocks the user searches for To use the API, you will need to create you account and get the free access token and paste it inside the get_stock function in the get_stock_info.py file at line 70 where key=sth

Running the Program: Run python project.py from the command line to start the app.

JSON Data File: accounts.json will store all user data, including usernames, hashed passwords, balances, and investment data.
