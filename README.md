# What the Software Does

The code in [findcarnegie.ipynb](https://github.com/nmcdowell00/lab6/blob/main/findcarnegie.ipynb) file allows you to query the [Carnegie Mellon Directory](https://directory.andrew.cmu.edu/). It does this by using the Python Library *Selenium* to remotely connect to the web page and enter certain search terms that *you* will specify. Selenium uses a process called webscraping to target certain elements websites codebase(building blocks of the website) and save what is stored within them. Webscraping is a bit confusing. If you want more clarification you can watch [this video](https://www.youtube.com/watch?v=Ct8Gxo8StBU&ab_channel=ParseHub).
  
# Installation Documentation 

Before you can begin to run the function you will need to download a few things. First you need to downlaod selenium which can done by entering
```pip install selenium``` in the commmand line. Now you need to install a webdriver manager. To do so, enter ```pip install webdriver-manager``` into your terminal. For good measure you should also update your Chrome(you need to use chrome for this function. Instructions for updating chrome can be found [here]("https://support.google.com/chrome/answer/95414?hl=en&co=GENIE.Platform%3DDesktop"). After all of this, you should be able to run the function. 
  
# How to Use it

This function is pretty simply to run. You will first want to clone the repository to your desktop. Now you can either open the *findcarnegie.ipynb* in Jupytr Notebooks and run the function, or using the command line to execute the *findcarnegie.py* function. All that the should be required of you to run the function is entering a name and a major. 



