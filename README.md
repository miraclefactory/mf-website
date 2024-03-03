# <img height="22" alt="mf-logo" src="https://github.com/miraclefactory/.github/assets/89094576/21774f34-ade2-45e3-966a-c2ff984af117"> Website

![www miraclefactory co_](https://user-images.githubusercontent.com/89094576/181905465-13b919fb-b708-4ab3-b7d1-cda12a4d5537.png)

## Visit Our Site 🌐
You can visit our website at [**miraclefactory.ai**](https://miraclefactory.ai/).   
Learn our goals and ideals, help us build a better community and a better world!  
Feel free to join our community and put your ingenuity to use :)

## You Can Contribute! 🌟
This is the public repo for the official website of Miracle Factory. We welcome every good idea, what ever the form. 
You can make suggestions and contributions on the website's:    
> * Content (writing style, typo, etc.)
> * Style (color, font, incompatibility with devices, smoothness optimization, etc.)
> * Security loopholes (please contact us via our public email)
> * Code optimizations (bad coding style, bugs, loopholes, etc.)
> * And more...

## Repository Maintenance 🔨
**ANY FORM** of content / style change should be submitted via Pull Requests.  
If you wish to make adjustments to this repo, please fork the **dev** branch of this repo and commit your change to your **dev** branch first, then create a PR to merge it into our **dev** branch, and we will then ask you to create another PR to merge your change into the **main** branch. This is because our **main** branch is for displaying only, and we created this hierarchy to control our development pipeline and keep our codebase organized.   
If you have any suggestions regarding this repo, please submit your idea via Issues.   
Feel free to make any reasonable improvements and suggestions!

## Configuration Notice ⚙️
This repo does not contain any of our app configs, please bear that in mind before running the website at your local development server. 
If you want to test all the app config related functionalities, please config your own:   
> * email_prefix
> * email_server
> * email_port
> * email_username
> * email_password
> * secret_key
> * security_password_salt
> * etc.  

For the full list, please check out the `CONFIG.md` file.

You can do so by creating a `.env` file under directory `/application/`. 
The `.gitignore` will auto ignore your file so that your configuration will not be pushed to GitHub. 
You should write something like: `email_username = "xxxx"` in your `.env` file, and the usage is well shown in `/application/__init__.py`, 
check it out in case you don't know how to use `python-decouple`.   

## How to Run ▶️
Before you run the application, please make sure that all the required python libraries are installed using: 
```
$ pip install -r requirements.txt
```
After that, you can simply run the website in your local development server (your terminal or shell) using `run.sh`: 
```
$ sh run.sh
```
You will need to have a sqlite database matching your SQLALCHEMY_DATABASE_URI config to access the database functionalities.
> **Notice:**   
> If you are using macOS Monterey or newer, please avoid using the Flask default port 5000, this will cause trouble because this port is already taken by AirPlay in newer systems. 

## Deployment 🚀
You don't need to worry about deployment, you can leave it to us :)
But if you have any suggestions, please feel free to submit your idea via Issues.
