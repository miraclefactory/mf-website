## A full list of what to put in your `.env` file

* email_prefix (1)
* email_server
* email_port
* email_username
* email_password
* secret_key
* security_password_salt
* database_uri
* auth_code (2)
* root_user_name (3)
* root_user_email (3)
* root_user_password (3)
* github_client_id (4)
* github_client_secret (4)
* upload_folder (5)


> (1) This should be your server domain, e.g. `http://localhost:5000/`, `https://miraclefactory.ai/`, **don't forget the trailing slash!**

> (2) This is a list of all the authentication codes for admin login, use the same syntax as a Python list, e.g. `["123456", "abcdef"]`.

> (3) This is the config of the root user, the root user is the first user created in the database, and it will be automatically given admin privileges.

> (4) This is the GitHub OAuth app config, you can create one in your GitHub Developer Settings. On registration, you will be given a client ID and a client secret, put them here.

> (5) This is the folder where all the uploaded avatars will be stored, **only a relative path is allowed**, e.g. `/static/user_assets/avatars/`, **don't forget the trailing slash!** It is preferable to use the `/static/user_assets/avatars/` directory as it is configured as ignored by the `.gitignore` file.
