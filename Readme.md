## Class-1
# what is selenium?
    1. Selenium is a suite which contains
        1. Selenium IDE
        2. Selenium WebDriver
        3. Selenium Remote Control (RC) (Deprecated)
        4. Selenium GRID

# what is selenium IDE?
     Selenium IDE is a browser extension that allows users to record and playback interactions with a web browser.
    
# what is selenium WebDriver?
    1. Selenium webdriver is a browser automation tool which is open-source used in automation testing, webscrapping etc.
    2. It supports multiple browsers, making it a versatile choice for cross-browser testing.
    3. It supports multiple programming languages like python, java, javascript, ruby etc.

# what is selenium Grid?
    1. Selenium Grid facilitates the parallel execution of tests across multiple machines and browsers. 
    2. It allows for the distribution of tests, making it possible to run tests concurrently on different environments.
    3. Selenium Grid is especially valuable for large-scale test automation and for testing across various browser and platform combinations.

    Alternatives for Selenium Grid:

        1. Docker with Selenium Containers:
            1. Using Docker containers for Selenium allows you to create isolated environments 
                for running tests on different browsers and versions. 
            2. Docker-compose can be used to orchestrate the containers, and this approach is becoming 
                increasingly popular for its ease of use and scalability.

        2. Kubernetes with Selenium Pods:
            1. Kubernetes is a container orchestration platform that can be used to deploy and manage Selenium Grid-like setups. 
            2. Selenium can be deployed as pods in a Kubernetes cluster, providing scalability and flexibility.

        3. BrowserStack:
            1. BrowserStack is a cloud-based testing platform that allows you to run Selenium tests on a variety of browsers and devices. 
            2. It provides a Selenium Grid in the cloud, eliminating the need for setting up and maintaining your own grid infrastructure. 
            3. It's a convenient solution for cross-browser testing.

    
# Basic Steps to write a script:
    1. Create a Service object to locate the driver path
    2. Create a driver Object
    3. navigate to URL
    4. maximize the browser window
    5. find element using locators
    6. Perform action(click,send_keys) on element 
    7. verify test
    8. quit driver

# locators in Selenium:
    1. id
    2. name
    3. linkText
    4. partialLinkText
    5. class
    6. Xpath

        1. Absolute Xpath
            1. Starts with single slash "/"
            2. captures full xpath (starts from beginning)
            3. /html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]
            4. Not prefferec

        2. Relative Xpath
            1. Starts with double slash "//"
            2. captures relative xpath (starts from anywhere from the webpage)
            3. //div[@class='featured-box cloumnsize1']//h4[1]//b[1]
            4. Preferred

    7. CSS Selector
            1. CSS Selector combines an element selector and a selector value that can 
                identify particular elements on a web page.
            2. Like XPath, CSS selector can be used to locate web elements
            3. Types of CSS Selectors:
                       1. ID (input#id) // input = tag
                       2. Class (input.classname)
                       3. Attribute (input[attributename = value])
                       

## Difference Between driver.close() and driver.quit()

    In Selenium Webdriver, driver.close() and driver.quit() are two methods for closing a browser window.
![img_2.png](img_2.png)


