from selenium import webdriver
import time
option = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,
    'download.default_directory': 'E:\\新联国际\\地产项目\\testRUn\\result'
}
option.add_experimental_option('prefs', prefs)
option.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=option)

driver.get('http://192.168.0.156:8085')
driver.find_element_by_xpath(
    '//*[@id="login"]/section/main/div/div[2]/form/div[1]/div/div/input'
).send_keys('test@mixgo.com')
driver.find_element_by_xpath(
    '//*[@id="login"]/section/main/div/div[2]/form/div[2]/div/div/input'
).send_keys('123456')
driver.find_element_by_xpath(
    '//*[@id="login"]/section/main/div/div[2]/button').click()
time.sleep(2)
table = driver.find_element_by_xpath(
    '//*[@id="home"]/section/section/main/div/div[2]/div/div[3]/table/tbody')

# table的总行数，包含标题
table_rows = table.find_elements_by_tag_name('tr')
print("总行数:", len(table_rows))
# 总列数
table_cols = table_rows[0].find_elements_by_tag_name('td')
print("总列数:", len(table_cols))


def seting(css, keys):
    time.sleep(2)

    lists = driver.find_element_by_xpath(css)
    tt = lists.find_elements_by_tag_name('li')
    print("总数:", len(tt))
    for i, name in enumerate(tt):
        print(name.text)
        if name.text == keys:
            tt[i].click()
            return

    # for i, name in enumerate(table_rows):
    #     for a, names in enumerate(table_cols):
    #         row1_col2 = table_rows[i].find_elements_by_tag_name('td')[a].text
    #         print("第%s行第%s列的text:" % (i, a), row1_col2)
    #         if row1_col2 == 'Edit':
    #             table_rows[i].find_elements_by_tag_name('td')[a].click()
    #             print('ss')


table_rows[0].find_elements_by_tag_name('td')[6].click()

# time.sleep(2)
# lists = driver.find_element_by_xpath(
#     '//*[@id="home"]/section/section/main/div/div[1]/ul')
# tt = lists.find_elements_by_tag_name('li')

seting('//*[@id="home"]/section/section/main/div/div[1]/ul', 'Email')

print('kkk')