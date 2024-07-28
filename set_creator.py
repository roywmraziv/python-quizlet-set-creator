from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_quizlet_set(data):
    # Start the Safari WebDriver
    driver = webdriver.Safari()
    
    # Open the Quizlet Create Set page
    driver.get("https://quizlet.com/create-set")
    
    # Wait for the login and manual navigation to the create set page if not automated
    input("Please log in and navigate to the create set page, then press Enter here...")

    try:
        # Wait until the form is loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "CreateSetTerms-termsList"))
        )
        
        # Find the elements for terms and definitions
        terms = driver.find_elements(By.CLASS_NAME, 'TermContent-side--word')
        definitions = driver.find_elements(By.CLASS_NAME, 'TermContent-side--definition')
        
        # Loop through the dictionary and fill in the terms and definitions
        for idx, (term, definition) in enumerate(data.items()):
            # If there are more terms than initial inputs, you may need to handle adding new rows
            if idx < len(terms):
                terms[idx].send_keys(term)
                definitions[idx].send_keys(definition)
        
        # Additional code to handle saving the set if needed
        print("Data entered successfully.")
        
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Keep the browser open for review, or you can use driver.quit() to close it automatically
        input("Press Enter to close the browser...")
        driver.quit()

# Example data
data = {
    "Python": "A high-level programming language",
    "Selenium": "A tool for automated testing of web applications"
}

fill_quizlet_set(data)