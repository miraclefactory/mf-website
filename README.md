# Official Website of Miracle Factory

![www miraclefactory co_](https://user-images.githubusercontent.com/89094576/181905465-13b919fb-b708-4ab3-b7d1-cda12a4d5537.png)
---

### Visit Our Site 🌐
You can visit our website at [**miraclefactory.co**](https://miraclefactory.co/).   
Learn our goals and ideals, help us build a better community and a better world!  
Feel free to join our community at the bottom of our website :)

### You Can Contribute! 🌟
This is the public repo for the official website of MiracleFactory. We welcome every good idea, what ever the form. 
You can make suggestions and contributions on the website's:    
> * Content (writing style, typo, etc.)
> * Style (color, font, incompatibility with devices, smoothness optmization, etc.)
> * Security loopholes (please contact us via our public email)
> * Code optimizations (bad coding style, bugs, loopholes, etc.)
> * And more...

### Repository Maintenace 🔨
**ANY FORM** of content / style change should be submitted via Pull Requests.   
If you have any suggestions regarding this repo, please submit your idea via Issues.   
Feel free to make any reasonable improvements and suggestions!

### Security Notice ⚠️
This repo does not contain any of our secret app configs, please bear that in mind when you are running the website at your local development server. 
If you want to test all the app config related functionalities, please config your own:   
> * MAIL_SERVER
> * MAIL_PORT
> * MAIL_USERNAME
> * MAIL_PASSWORD
> * SECRET_KEY
> * SECURITY_PASSWORD_SALT
> * SQLALCHEMY_DATABASE_URI

You can do so by creating a `.env` file under directory `/application/`. 
The `.gitignore` will auto ignore your file so that your configuration will not be pushed to GitHub. 
You should write something like: `email_username = "xxxx"` in your `.env` file, and the usage is well shown in `/application/__init__.py`, 
check it out in case you don't know how to use `python-decouple`.   

### How to Run ▶️
You can simply run the website in your local development server (your terminal or shell) using `run.sh`: `sh run.sh`.   
You will need to have a sqlite database under `/application/database/` to access the database functionalities.
> ##### Notice
> If you are using macOS Monterey or newer (macOS Ventura), please avoid using the Flask default port 5000, 
this will cause trouble because this port is already taken by AirPlay in these systems.   

### TO DO List
> 1. concurrency control(Threadpool executor) ✓
> 2. database connection and query ✓
> 3. python file restructuring ✓
> 4. spam protection ✓
> 5. speed optimization
> 6. security enhancement
> 7. deployment ✓
> 8. database functions
