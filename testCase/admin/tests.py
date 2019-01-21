

import sys
import os
import re
# 添加环境变量，os.path.dirname()可根据文件夹所处深度进行调整
dw = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(dw))
# print(dw)

import readConfig
from common.cose import PySelenium
from common.configxls import readExcle





xls = readExcle()
rd = readConfig.ReadConfig()

test = rd.rd_json('testCase\Id_value.json')


for i in  test:
    print(i)



sm = PySelenium('chrome')
sm.openUrl('http://192.168.0.156:8085')

sm.addText('xpath,//*[@id="login"]/section/main/div/div[2]/form/div[1]/div/div/input','test@mixgo.com')
sm.addText('xpath,//*[@id="login"]/section/main/div/div[2]/form/div[2]/div/div/input','123456')
sm.click('xpath,//*[@id="login"]/section/main/div/div[2]/button')


# 使用表格形式添加项目
# sm.addText("xpath,//*[@id='projectFile']",R"E:\新联国际\地产项目\testRUn\testFile\Project Template to Create Project Entry.xlsx")
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/div/div[2]/div/button[2]/span')
# sm.sleeps()
# 刷新功能按钮
# # sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/div/div[1]/button')
# # sm.sleeps()
# 获取第一行项目名称
# a = sm.getText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]')
# print(a)

# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/div/div[2]/button/span')

# 进入项目编辑页面

sm.sleeps()

table = sm.getElement('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[3]/table')
sm.sleeps()
#table的总行数，包含标题
table_rows = table.find_elements_by_tag_name('tr')
# 总列数
print(len(table_rows))
table_cols = table_rows[0].find_elements_by_tag_name('td')
print(len(table_cols))

# for i,name in enumerate(table_rows):
#     for a,names in enumerate(table_cols):
#         row1_col2 = table_rows[i].find_elements_by_tag_name('td')[a].text
#         print ("第%s行第%s列的text:"%(i,a),row1_col2)
#         if row1_col2 == 'Edit':
#             table_rows[i].find_elements_by_tag_name('td')[a].click()
#             break 
    
#     break

sm.lists_click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[3]/table/tbody','Edit',row=0)

sm.sleeps()

sm.list_click('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul','Settings')


sm.moveToTargetElement('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[6]/div')


# sm.list_click('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul','Media')



sm.list_click('css,.el-menu--horizontal > ul','Image')
sm.moveToTargetElement('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[6]/div')

sm.list_click('css,.el-menu--horizontal > ul','PDF')
sm.moveToTargetElement('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[6]/div')

sm.list_click('css,.el-menu--horizontal > ul','Video')


# # 添加其他公司按钮
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/button[1]')





# sm.list_click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div','66','label')

# ss = sm.getText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]')

# na = ss.strip(',').split('\n')
# print(na)


# sm.sleeps()
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div/button')

# sm.addText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div/div/div[1]/input','CommercialResidential')





# print(d.text)

# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div/div/div/span')
# sm.Dropdown_box('/html/body/div[2]/div[1]/div[1]/ul/li','Commercial/Residential')
# /html/body/div[4]/div[1]/div[1]/ul/li[1]
# sm.selectByValue('//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[5]/div[1]/div/div/div/div/span','Commercial/Residential')

# Description 富文本编辑器
# sm.sleeps()
# sm.switchFrame('id,description_ifr')

# sm.addText('id,tinymce','adsgsdfag')


# sm.switchFrameOut()
# # sm.addText('xpath,//*[@id="keyPoints_ifr"]','adsgsdfag')
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[1]/div/div[2]/button[1]')
# sm.sleeps()
# print(sm.getText('xpath,/html/body/div[2]/div/div[1]/p'))

# sm.sleeps()
# sm.click('link_text,Detail')
# sm.sleeps()
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[4]')
# sm.Dropdown_box('//*[@id="home"]/section/section/main/div/div[1]/ul/li','Building/Phases')

# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[2]')


# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[1]/div/div[2]/button[1]')
# sm.addText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/input','233')
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/button[1]')

# sm.sleeps()
# sm.addFile('xpath,//*[@id="concatImgFile"]',sm.Box_File(R'testFile\image\test.png'))

# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/button')
# # sm.sleeps(5)

# sm.click('css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary')

# print(sm.isEnabled('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[23]/div[2]/div/span[2]'))


# a = 26
# for i in range(5):
    
#     sm.addText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[%s]/div[1]/div/div/div/input'%a,'名称%s'%i)
#     sm.addText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[%s]/div[2]/div/div/div/input'%a,'值%s'%i)            
#     a = a+1
#                     #   //*[@id="home"]/section/section/main/div/div[2]/div/div[2]/form/div[27]/div[1]/div/div/div/input



# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[3]')



# a = re.sub("\D", "", sm.getText('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[3]/div[1]/div[1]/div'))
# print (type(a))

# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[1]/ul/li[4]')
# 通过xls添加数据
# sm.addFile('id,unit',rd.Box_File(R'\testFile\UnitExport.xls'))
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button[2]')
# sm.sleeps()
# # 下载已添加数据
# sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/button')



# a = xls.read_col(rd.Box_File(R'\result\UnitExport.xls'),'Floor')
# if a[1:-1] != '':
#     print(a)

# 是否修改户型状态勾选框
sm.click('xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[1]/div[3]/label/span[1]')



sm.sleeps(5)




sm.quit()
