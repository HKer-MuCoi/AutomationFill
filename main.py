import openpyxl
from selenium import webdriver
import time
#web = webdriver.Firefox()
web = webdriver.Chrome()
file_location = r"C:\Users\Admin\Documents\Python fun PJ\Auto_Read_Excel\hn.xlsx"
wb = openpyxl.load_workbook(file_location)
sheet1 = wb['HN']
# sheet1 = wb.get_sheet_by_name('HN')
col_taken = [2, 7, 8]

# for i in sheet1.max_rows:
for i in range(7000, 8000):
    arr_data = []
    for j in col_taken:
        arr_data.append(sheet1.cell(row=i, column=j).value)
    #Extract data
    bob = arr_data
    print("Name: " + bob[0] + " |Tel: " + str(bob[1]) + " |Mail: " + bob[2])

    #Start
    if ((bob[0] != None) and (str(bob[1]) != None) and bob[2] != None):
        nameFill = bob[0]
        phoneFill = str(bob[1])
        emailFill = bob[2]
    else:
        if bob[0] == None:
            nameFill = "No Name"
            phoneFill = str(bob[1])
            emailFill = bob[2]
        elif str(bob[1]) == None:
            nameFill = bob[0]
            phoneFill = "No Phone"
            emailFill = bob[2]
        elif str(bob[1]) == None:
            nameFill = bob[0]
            phoneFill = str(bob[1])
            emailFill = "No Mail"
    web.get('https://vug.dosi-in.com/vug-2021-dh-thuong-mai-bai-du-thi-vong-loai-2-dance-battle-ha-noi?fbclid'
        '=IwAR0gEEgGQ4yGFwCRB9HEdAmXToMnpGOVFFGE-pu36kIgr1g8FiYViA7cSbQ')
    time.sleep(1)

    name = web.find_element_by_xpath('//*[@id="name-vote"]')
    name.send_keys(nameFill)

    phone = web.find_element_by_xpath('//*[@id="phone"]')
    phone.send_keys(phoneFill)

    email = web.find_element_by_xpath('//*[@id="email-vote"]')
    email.send_keys(emailFill)

    submitBtn = web.find_element_by_xpath('//*[@id="app"]/main/section/div/form/button')
    submitBtn.click()
    #Time for submit
    time.sleep(1)


