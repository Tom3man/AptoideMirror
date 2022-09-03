# AptoideMirror 

This project is a Flask-based webframework application built around webscraping the [Aptoide website](https://en.aptoide.com/) using the BeautifulSoup package.  
By spinning up the application, the user can enter an app-specific URL from the Apatoid website and have the following returned: 

- App's name 
- App's version 
- Number of downloads 
- Description for the current version 
- Release date 


# Deployment 

To deploy the webframework application. install all packages contained in the requirements.txt file (we recommended doing this in a Python virtual environment as there may be some cross dependencies).  
Once this is done the framework can be initiated by running the main.py script found in the in the aptoid_mirror folder.  

`python -m main.py` 

This will spin up the webserver and by navigating to the [local host](http://localhost:5000/) URL (default port 5000) the user may begin interacting. 
