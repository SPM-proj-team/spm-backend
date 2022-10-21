from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
import time
import helper_function

def updateRoleTest(driver,backend_url,frontend_url):
    # going to admin page
    adminBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin']"))
    )
    adminBtn.click()

    # test update and delete role
    createUpdateRoleBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Update & Delete Roles']"))
    )
    try:
        createUpdateRoleBtn.click()
        helper_function.testFormatSingle("Going to Update & delete Roles", True)
    except:
        helper_function.testFormatSingle("Going to Update & delete Roles", False)
        

    prevSlaveRoleRequest = requests.get(backend_url+"roles/1")
    prevSlaveRoleSST = json.loads(prevSlaveRoleRequest.text)["data"][0]
    prevSlaveSkillCount = len(prevSlaveRoleSST["Skills"])

    RoleSearchBar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='jobRoleInputText']"))
    )
    RoleSearchBar.send_keys("slave")
    jobRole = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[text()='Operation Slave']"))
    )
    jobRole.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    description = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='description']"))
    )
    description.send_keys("Please promote me. Slavery is no go.")
    # jobRoleInputText
    
    addSkillBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='+ Add Skills']"))
    )
    time.sleep(2)
    addSkillBtn.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    skillSearch = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[@id='jobRoleInputText']"))
    )
    
    skillSearch[1].send_keys("adobe")
    
    addSkill = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()=' + Add ']"))
    )
    addSkill.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    save = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Update']"))
    )
    save.click()
    time.sleep(5)
    slaveRoleRequest = requests.get(backend_url+"/roles/1")
    slaveRoleSST = json.loads(slaveRoleRequest.text)["data"][0]
    slaveSkillCount = len(slaveRoleSST["Skills"])
    helper_function.testFormatCount("Updated No. Of Skills", slaveSkillCount, prevSlaveSkillCount+1)

    # # fixed the data back to original
    # jsonstr = '{"Job_ID":1,"Job_Role":"Operation Slave","Job_Title":"Staff","Department":"Operations","Description":"Slavery is no go. Please promote me","Skills":["S001","S002","S003","S005","S006"]}'
    # requestFixed= requests.put(backend_url+"/roles",  json = json.loads(jsonstr))

def createRoleTest(driver,backend_url,frontend_url):
    prevRoleRequest = requests.get(backend_url+"roles")
    prevRoleCount = len(json.loads(prevRoleRequest.text)["data"])
    

    driver.get(frontend_url)
    #  go to admin page
    adminBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin']"))
    )
    adminBtn.click()
    createCreateRoleBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Create New Roles']"))
    )
    createCreateRoleBtn.click()
    jobRoleNameInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='job_role']"))
    )
    jobRoleNameInput.send_keys("job role name test")

    jobRoleTitle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='job_Title']"))
    )
    jobRoleTitle.send_keys("job role title test")
    # //select[@id='department']
    department = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='department']/option[text()='Executive Management']"))
    )
    department.click()
    time.sleep(2)
    description = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='description']"))
    )
    description.send_keys("job description test")

    addSkillBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='+ Add Skills']"))
    )
    addSkillBtn.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    skillSearch = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[@id='jobRoleInputText']"))
    )
    # print(len(skillSearch))
    skillSearch[0].send_keys("adobe")
    
    addSkill = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()=' + Add ']"))
    )
    addSkill.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    create = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='create-btn']"))
    )
    create.click()
    time.sleep(2)
    RoleRequest = requests.get(backend_url+"roles")
    RoleCount = len(json.loads(RoleRequest.text)["data"])
    return helper_function.testFormatCount("Updated No. Of Roles", RoleCount, prevRoleCount+1)

def deleteRoleTest(driver,backend_url,frontend_url):
    driver.get(frontend_url)
    adminBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin']"))
    )
    adminBtn.click()
    time.sleep(2)

    # test update and delete role
    createUpdateRoleBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Update & Delete Roles']"))
    )
    createUpdateRoleBtn.click()
    helper_function.testFormatSingle("Going to Update & delete Roles", True)

    prevRoleRequest = requests.get(backend_url+"roles")
    prevRoleCount = len(json.loads(prevRoleRequest.text)["data"])

    RoleSearchBar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='jobRoleInputText']"))
    )
    RoleSearchBar.send_keys("operation slave")
    jobRole = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[text()='Operation Slave']"))
    )
    jobRole.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    delete = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='delete-btn']"))
    )
    delete.click()
    time.sleep(2)
    delConfrim = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete']"))
    )
    delConfrim.click()
    time.sleep(2)
    RoleRequest = requests.get(backend_url+"roles")
    RoleCount = len(json.loads(RoleRequest.text)["data"])
  
    return helper_function.testFormatCount("Delete No. Of Roles", RoleCount, prevRoleCount-1)

def SearchRoleTest(driver,backend_url,frontend_url):
    driver.get(frontend_url)
    viewRoleBtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/JobRoles']"))
    )
    viewRoleBtn.click()
    searchBarRole = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='floatingInput']"))
    )
    searchBarRole.send_keys("operation")
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'card-body w-100 text-start')]"))
    )
    return helper_function.testFormatCount("Search result Count",len(result),3)