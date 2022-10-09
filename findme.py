def do_i_have_a_twin():
   
    #collects inputs
    full_name = input("enter your first and last name").lower()
    department = input("enter your department name aka your major").lower()

    #convert inputs to strings
    full_name = str(full_name)
    
    #imports trys and exceptions implemented by cj
    try:
        #imports
        import requests
        from selenium import webdriver  
        import time  
        from selenium.webdriver.common.keys import Keys  
        from webdriver_manager.chrome import ChromeDriverManager
        
        inputs_worked(full_name, department)
        
    except:
         
        print("Hello,", full_name, "We know 3 things about you: \n\nThe first of course is your name \nThe second is that your department is", department)
        print("And third is that you do not have selenium or webdriver_manager installed on your device, which is required to use this scrapping program\n")
        print("you can install these with pip install in the terminal if desired, if not thank you for visiting our program!")

#function designed by nate  
def inputs_worked(full_name, department):
    #split string into first and last name
    first_name = full_name.split(" ")[0]
    last_name = full_name.split(" ")[1]
    try:
        print("sample test case started")  
        #virtual chrome driver; must have chrome for it to work
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

        #driver = webdriver.Chrome("/Users/natemcdowell/Desktop/chromedriver-2")  

        #desired page
        driver.get("https://directory.andrew.cmu.edu/")  

        #input the name into the search bar
        search_box = driver.find_element("name", "search")
        search_box.send_keys(full_name)
        time.sleep(3) 

        #click the button
        button = driver.find_element("name","action")
        button.send_keys(Keys.ENTER) 

        #loops through first names
        first_count = 0
        for x in driver.find_elements("xpath",".//tr/td[2]"):
            name = x.text.lower()
            if name == first_name:
                first_count+=1

        #loops through last names
        last_count = 0
        for x in driver.find_elements("xpath",".//tr/td[1]"):
            name = x.text.lower()
            if name == last_name:
                last_count+=1

        #loops through departments
        dpmt_count = 0
        for x in driver.find_elements("xpath",".//tr/td[4]"):
            dpmt_scrape = x.text.lower()
            if dpmt_scrape == department:
                dpmt_count += 1



        print("there are", first_count,"people with your first name and",last_count, "people with your last name")
        print("out of all similar names, first or last, there are",dpmt_count,"in your department")

    except:
        print("search returned no results")
    
do_i_have_a_twin()