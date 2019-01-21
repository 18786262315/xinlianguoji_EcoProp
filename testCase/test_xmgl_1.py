# --*-- coding:utf-8 --*--
import HTMLTestRunner
import unittest
import re
from common.Log import Logger
from common.cose import PySelenium
import readConfig
from common.configxls import readExcle

xls = readExcle()
rd = readConfig.ReadConfig()
sm = PySelenium("chrome")
sm.openUrl(rd.get_http("baseurl"))
element = rd.rd_json(R"testCase\Id_value.json")


class MyTest(unittest.TestCase):  #继承unittest.TestCase
    """
    项目基本信息管理列表
    """

    @classmethod
    def setUpClass(cls):
        print("开始执行test_main---->")
        sm.getScreenshot(R"result\进入登录页面.png")
        sm.wait(10)

    @classmethod
    def tearDownClass(cls):
        print("end----->")
        sm.quit()

    def test_run(self):
        """登录系统"""
        sm.addText(element.get("login_name"), rd.get_user("email"))
        sm.addText(element.get("login_pss"), rd.get_user("password"))
        sm.click(element.get("login_boutten"))
        # a = sm.getText(
        #     "xpath,//*[@id='home']/section/section/header/div/div[1]")
        # print(a)
        sm.getScreenshot(R"result\进入系统.png")
        # self.assertEqual("Background Management", a)
    # @unittest.skip(u"跳过测试！")
    def test_run1(self):
        """添加项目"""
        css = 'css,.el-table__body-wrapper.is-scrolling-none > table'
        

        # sm.addFile(element.get("Properties_input"),rd.Box_File(R"\testFile\Project Template to Create Project Entry.xlsx"))
        # sm.click(element.get('Properties_import'))
        # sm.sleeps()
        # 刷新项目列表
        sm.click( element.get('Properties_Refresh'))
        ts = sm.tables(css,0,0)
        print(ts)
        self.assertEqual("testing2", ts, msg="添加项目成功")


    @unittest.skip(u"跳过测试！")
    def test_run2(self):
        """下载项目列表"""
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/div/div[2]/button/span"
        )
        sm.sleeps()
        sm.getScreenshot("result\\下载项目列表.png")

    @unittest.skip(u"跳过测试！")
    def test_run3(self):
        """进入项目编辑页面"""

        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div/button"
        )
        # a = sm.getText(
        #     "xpath,//*[@id='home']/section/section/main/div/div[1]/div/span[2]"
        # )
        # print(a)
        sm.getScreenshot(R"result\进入项目详情页面.png")
        # self.assertEqual("testing2", a)

    @unittest.skip(u"跳过测试！")
    def test_run4(self):
        """Detail 模块内容修改"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Detail")

        # Sync To Mobile
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[1]/div[1]/div/div/label"
        )
        # Is Featured
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[1]/div[2]/div/div/label"
        )
        # Currency Symbol
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/input",
            "$")
        # Developer
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/input",
            "MixGo")
        # Type 动态下拉列表处理未实现
        # sm.click("xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div/div/div/span")
        # type_text填写
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div/input",
            "Individual Title Bungalow")
        # Number of Units 总户型数
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[1]/div/div/div/input",
            "401")
        # Number of Units Alt Text
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[2]/div/div/div/input",
            "333")
        # Tenure 动态下拉列表处理未实现
        # -----
        # Tenure Alt Text 产权年限
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[5]/div[2]/div/div/div/input",
            "60 years")
        # Completion/TOP Date 交房日期
        # ----
        # Completion/TOP Date Alt Text
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[6]/div[2]/div/div/div/input",
            "22-Dec-2019")
        # Launch Date 开盘日期
        # ---
        # Launch Date Alt Text
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[7]/div[2]/div/div/div/input",
            "21-Dec-2019")
        # Country	项目所在国家名称
        # ----
        # Country Alt Text
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[8]/div[2]/div/div/div/input",
            "中国")
        # Location	预设的行政区
        # ---
        # Location Alt Text
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[9]/div[2]/div/div/div/input",
            "深圳")
        # Property Group	自定义的行政区，用于对应在前端Project页面中的项目所属的行政区
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[10]/div[1]/div/div/div/input",
            "深圳")
        # Map Zoom Level	地图可放大的倍数
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[10]/div[2]/div/div/div/input",
            "2")
        # Laitude	用于Google Map的维度
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[11]/div[1]/div/div/div/input",
            "22.636681180511182")
        # Longitude	经度
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[11]/div[2]/div/div/div/input",
            "114.04098977062986")
        # Street Addres  详细地址
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[12]/div[1]/div/div/div/textarea",
            "U创谷")
        # Postal Code	邮政编码
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[12]/div[2]/div/div/div/input",
            "518000")

        values = """
        富文本测试内容:
            中文：啦啦啦
            英文：AbcD2*&%￥ sad
            数字：123456767890
            特殊符号：<$%#@$()>:;\/\/``~~
        """
        # Description 用于描述项目详情 富文本编辑器
        sm.switchFrame("id,description_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        # keyPoints 卖点 富文本编辑器
        sm.switchFrame("id,keyPoints_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        # Facilities 项目内的配套设施 富文本编辑器
        sm.switchFrame("id,facilities_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        # Nearby Amenities	周边配套设施
        sm.switchFrame("id,nearbyAmenities_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        # commission
        sm.switchFrame("id,commission_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        # externalCommission
        sm.switchFrame("id,externalCommission_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        # salesContacts
        sm.switchFrame("id,salesContacts_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()

        # 添加联系方式图片
        pd = rd.Box_File(R"\testFile\image\test.png")
        keys = sm.isElementExist(
            "//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[23]/div[2]/div/span[2]"
        )
        if keys:
            sm.click(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[23]/div[2]/div/span[2]"
            )
        sm.addFile("id,concatImgFile", pd)
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[23]/div/div/div/div/button[2]"
        )
        sm.sleeps()
        # 删除数据
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[23]/div[2]/div/span[2]"
        # )

        # 添加自定义字段内容
        a = 26
        for i in range(5):
            # name 名称
            sm.addText(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[%s]/div[1]/div/div/div/input"
                % a, "名称%s" % i)
            # value 值
            sm.addText(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[%s]/div[2]/div/div/div/input"
                % a, "值%s" % i)
            a = a + 1

        # 保存修改内容
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/div[2]/button[1]"
        )

        vlaue = sm.getText("xpath,/html/body/div[2]/div/div[1]/p")
        print(vlaue)
        self.assertEqual("Sucessful operated", vlaue)

    @unittest.skip(u"跳过测试！")
    def test_run5(self):
        """Building/Phases 模块"""

        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Building/Phases")

        # keys = sm.getText(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/div[1]/div/span"
        # )
        # a = re.sub(r"\D", "", keys)
        # if a != 0:
        #     for i in range(int(a)):
        #         sm.click(
        #             "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/button"
        #         )
        #         # 确认弹窗删除已添加内容
        #         sm.click(
        #             "css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
        #         )
        #         sm.click('css,body > div.el-notification.right > div > div.el-notification__closeBtn.el-icon-close')

                # sm.sleeps(0.5)
        keys = ["54","56","58","60","54A","54B","54C","54D","54E","54F","54G","54H","54J","56A","56B","56C","56D","56E","56F","56G","56H","56J","56K","56L","56M","56N","58A","58B","58C","58D","58E","58F","58G","58H","58J","58K","58L","58M","58N","60A","60B","60C","60D","60E","60F","60G","60H","60J","60K","60L","Block 50","Block 50A","Block 52","Block 62","Block 62A","Block 64","Block 64A","Block 66","Block 66A","Block 68","Block 68A"]
        for i in keys:
            sm.sleeps(0.5)
            sm.click(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/div[2]/button[1]/span"
            )
            sm.addText(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/input",
                i)
            sm.click(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/button[1]"
            )
            sm.click('css,body > div.el-notification.right > div > div.el-notification__closeBtn.el-icon-close')

        # print(sm.getText("xpath,/html/body/div[2]/div/div[1]/p"))
        # 修改内容
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[3]/div/button/span"
        # )
        # sm.addText(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/input",
        #     rd.suiji())
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/button[1]"
        # )
        # print(sm.getText("xpath,/html/body/div[2]/div/div[1]/p"))
        # # 删除内容
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/button"
        # )
        # # 弹窗删除确认
        # sm.sleeps()
        # sm.click(
        #     "css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
        # )
        # 弹窗取消
        # sm.click("css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button:nth-child(1)")
        # vlaue = sm.getText("xpath,/html/body/div[2]/div/div[1]/p")

        # self.assertEqual("Sucessful operated", vlaue)

    @unittest.skip(u"跳过测试")
    def test_run6(self):
        """Floor Plans模块"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Floor Plans")

        k = sm.getText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[1]/div"
        )
        a = re.sub("\D", "", k)
        if a != 0:
            for i in range(int(a)):
                sm.click(
                    "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr/td[4]/div/button"
                )
                # 确认弹窗删除已添加内容

                sm.click(
                    "css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
                )
                # sm.sleeps(0.5)
        # 单个内容添加
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[2]/button[1]"
        )

        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div/input",
            "A-01")
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/input",
            "test1")
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr/td[5]/div/button[1]"
        )

        # 单张添加
        A01 = rd.Box_File(R"\testFile\image\A-01.png")
        sm.addFile("id,floorImage", A01)
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div/button[2]"
        )
        sm.sleeps()
        sm.getScreenshot(rd.Box_File(R"\result\添加单个户型图.png"))

        # 删除已添加内容
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button"
        )
        sm.click(
            "css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
        )
        sm.sleeps()
        # 通过表格添加内容
        FloorPlan = rd.Box_File(R"\testFile\FloorPlan.xls")
        sm.addFile("id,floorFile", FloorPlan)
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button[2]"
        )
        sm.sleeps()
        # 下载已添加的内容
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/button"
        )

        # 批量添加户型图
        pd_zip = rd.Box_File(R"\testFile\image\foorm.zip")
        sm.addFile("id,floorImage", pd_zip)
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div/button[2]"
        )
        #
        sm.getScreenshot(rd.Box_File(R"\result\批量添加户型图.png"))

        k = sm.getText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[1]/div"
        )
        a = re.sub(r"\D", "", k)
        # for i in range(int(a)):
        #     sm.click(
        #         "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button"
        #     )
        #     # 确认弹窗删除已添加内容
        #     sm.click(
        #         "css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
        #     )
        #     # sm.sleeps(0.5)
        print(a)
        sm.getScreenshot(rd.Box_File(R"\result\批量删除户型图.png"))

    @unittest.skip(u"跳过测试！")
    def test_run7(self):
        """untils 户型数据管理模块"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Untils")

        # 通过xls添加数据 untils
        sm.addFile("id,unit", rd.Box_File(R"\testFile\UnitExport.xls"))
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button[2]"
        )
        sm.sleeps()
        # 下载已添加数据
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/button"
        )

        # 是否修改户型状态勾选框 ,验证流程较为复杂，延迟处理
        # sm.click("xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[3]/label/span[1]")
        # 上传户型状态
        sm.addFile("id,unitTransaction",
                   rd.Box_File(R"\testFile\UnitTransactionsExport.xls"))
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div/button[2]"
        )
        sm.sleeps()
        # 下载当前所有户型的状态列表
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/button"
        )
        sm.getScreenshot(rd.Box_File(R"\result\户型管理页面.png"))

    @unittest.skip(u"跳过测试！")
    def test_run8(self):
        """Site/Stack Plans 模块"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Site/Stack Plans")

        keys = sm.getText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[1]/div"
        )
        a = re.sub(r"\D", "", keys)
        if a != 0:
            for i in range(int(a)):
                sm.click(
                    "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/button"
                )
                # 确认弹窗删除已添加内容
                sm.click(
                    "css,body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary"
                )
                # sm.sleeps(0.5)

        # 生成siteplan，以及All Buildings
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[2]/button[1]"
        )
        # 生成固定Table
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[2]/button[2]"
        )
        # 载入已创建的plans
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[2]/button[3]"
        )
        # 修改内容并保存
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button"
        )
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div/input",
            "siteplans")
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/label/span/span"
        )
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]"
        )
        # 重新生成siteplan
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[2]/button[1]"
        )

        sm.getScreenshot(rd.Box_File(R"\result\修改内容并重新生成平面图.png"))

        # 添加图片进行内容匹配
        sm.addFile("id,planFile",
                   rd.Box_File(R"\testFile\image\SiteStack_Plans_ing.zip"))
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button[2]"
        )
        sm.sleeps(1.5)
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/button"
        )

        # 添加图形功能按钮,添加正方形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/label[1]"
        )
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/button"
        )
        # 添加圆形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/label[2]"
        )
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/button"
        )
        # 添加三角形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/label[3]"
        )
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/button"
        )
        sm.getScreenshot(rd.Box_File(R"\result\添加图形.png"))
        # 复制图形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/button[1]"
        )
        # 粘贴图形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/button[2]"
        )
        # 删除选中图形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/button[3]"
        )

        # 弹出选择列表
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[4]/form/div/div[2]/div/div/div/div/span"
        )
        # 选择内容展示无法实现
        # ------
        # 点击serve功能按钮
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[4]/form/div/div[2]/button"
        )
        # 删除所有图形
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/button[4]"
        )
        # 保存所有内容
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/div/div[2]/button"
        )
        # 返回
        sm.click("xpath,//*[@id='home']/section/section/main/div/h1/button")

    @unittest.skip(u"跳过测试！")
    def test_run9(self):
        """Media项目文件模块"""
        #  --------image--------------
        sm.moveToTargetElement("css,.child_header > ul > li:nth-child(6)")
        sm.list_click("css,.el-menu--horizontal > ul", "Image")

        # 清空列表
        sm.list_del(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[1]/div",
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/button"
        )
        # # 批量添加
        # sm.addFile("id,imageFile", rd.Box_File(R"\testFile\image\project.zip"))
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button[2]"
        # )
        # sm.sleeps()

        # # 主图添加
        # sm.addFile("id,mainImageFile",
        #            rd.Box_File(R"\testFile\image\mainImage.png"))
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/div/button[2]"
        # )
        # sm.sleeps()
        # # 主图下载
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/button"
        # )

        # # 刷新列表
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[2]/button[2]"
        # )

        # 单个添加内容
        # image_url = R"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544682921175&di=50973efe8463e3e478ef9ae86b1d8280&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Fbd315c6034a85edf0284c80d42540923dd547597.jpg"
        # sm.click(
        #     "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[3]/div[1]/div[2]/button[1]"
        # )
        css = 'css,.el-table__body-wrapper.is-scrolling-none > table '
        send = '.el-input__inner'
        # sm.tables(css,0,0,'New_Url_image',send)
        # sm.tables(css,0,1,image_url,send)
        # sm.tables(css,0,3,cs_name='.cell > button:nth-child(1)')
        # ks = sm.tables(css,0,0)
        # print(ks)
        # self.assertEqual("New_Url_image", ks)

        # # 修改已添加内容
        # sm.tables(css,0,3)
        # sm.tables(css,0,0,"New_Url_image_set",send)
        # # sm.tables(css,0,1,image_url2,send) #修改的内容
        # sm.tables(css,0,3,cs_name='.cell > button:nth-child(1)')
        # ks = sm.tables(css,0,0)
        # print(ks)
        # self.assertEqual("New_Url_image_set", ks)

        # ------------PDF-------------

        sm.moveToTargetElement("css,.child_header > ul > li:nth-child(6)")
        sm.list_click("css,.el-menu--horizontal > ul", "PDF")

        # 删除所有已添加的PDF
        sm.list_del(
            "css,.col_text.el-col.el-col-12",
            "css,table > tbody > tr:nth-child(1) > td.el-table_3_column_17 > div > button"
        )

        # 批量添加PDF
        sm.addFile("id,pdfFile", rd.Box_File(R"\testFile\PDF\pdfFile.zip"))
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div[1]/div[2]/div/button[2]"
        )

        # 刷新列表
        sm.sleeps(3)
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div[1]/div[2]/button[2]"
        )
        # 获取当前列表数量
        naber = sm.getText(
            'xpath,//*[@id="home"]/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]'
        )
        a = re.sub(r"\D", "", naber)
        # self.assertEqual('4', a)

        # # 通过url添加PDF
        # sm.click("css,.col_button.el-col.el-col-12 > button:nth-child(1)")
        # sm.tables(css, 0, 0, "add_new_PDF_url", send)
        # sm.tables(css, 0, 1)
        # sm.tables(css, 0, 2)
        # # sm.tables(css,0,3,'http://www.pdf995.com/samples/pdf.pdf',send)
        # sm.tables(css, 0, 4, "input_new_PDF_Description", send)
        # sm.tables(css, 0, 6, cs_name='.cell > button:nth-child(1)')
        # text_name = sm.tables(css, 0, 0)
        # self.assertEqual("add_new_PDF_url", text_name)

        # 编辑已添加的PDF信息
        sm.tables(css, 0, 6)
        sm.tables(css, 0, 0, "Edit_PDF_name", send)
        sm.tables(css, 0, 1)  #勾选Is Sensitive
        sm.tables(css, 0, 2)  #勾选Restrict Email
        # sm.tables(css,0,3,'http://www.pdf995.com/samples/pdf.pdf',send)
        sm.tables(css, 0, 4, "Edit_PDF_Description", send)
        sm.tables(css, 0, 6, cs_name='.cell > button:nth-child(1)')
        text_name = sm.tables(css, 0, 0)
        # self.assertEqual("Edit_PDF_name", text_name)

        # --------------VIDEO------------

        sm.moveToTargetElement("css,.child_header > ul > li:nth-child(6)")
        sm.list_click("css,.el-menu--horizontal > ul", "Video")

        delt = "css,table > tbody > tr:nth-child(1) > td.el-table_6_column_37 > div > button"
        sm.list_del("css,.col_text.el-col.el-col-12", delt)
        sm.click('css,.col_text.el-col.el-col-8')
        # 单个文件添加.col_button.el-col.el-col-16 > div > button:nth-child(2)
        sm.addFile('id,videoFile', rd.Box_File(R'\testFile\Video\video1.mp4'))
        sm.click('css,.col_button.el-col.el-col-16 > div > button:nth-child(2)')
        sm.sleeps(5)
        vd_name = sm.tables(css, 0, 0)
        # self.assertEqual("video1", vd_name)
        # 批量Zip添加
        sm.addFile('id,videoFile', rd.Box_File(R'\testFile\Video\voide.zip'))
        sm.sleeps(5)
        sm.click(
            'css,col_button.el-col.el-col-12 > button:nth-child(2)')
        naber = sm.getText('css,.col_text.el-col.el-col-12')
        a = re.sub(r"\D", "", naber)
        # self.assertEqual('3', a)
        sm.sleeps(3)
        # 刷新列表
        sm.click(
            'css,col_button.el-col.el-col-12 > button:nth-child(2)')
        # 通过url添加视频
        video_url = 'https://www.mixgo.com/static/media/mixgo_scan.e3e8cc5.mp4'
        sm.click(
            'css,.col_button.el-col.el-col-16 > div > button:nth-child(1) ')
        sm.tables(css, 0, 0, 'input_new_Video_name', send)
        sm.tables(css, 0, 1, video_url, send)
        sm.tables(css, 0, 2, 'input_new_Video_Description', send)
        sm.tables(css, 0, 4, cs_name='.cell > button:nth-child(1)')
        sm.sleeps(3)
        # 编辑视频
        sm.tables(css, 0, 4)
        sm.tables(css, 0, 0, 'set_new_Video_name', send)
        sm.tables(css, 0, 1, video_url, send)
        sm.tables(css, 0, 2, 'set_new_Video_Description', send)
        sm.tables(css, 0, 4, cs_name='.cell > button:nth-child(1)')


    @unittest.skip(u"跳过测试！")
    def test_run10(self):
        """Email模块"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Email")

        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[2]/div/div/div/div/input"
        )
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[2]/div/div/div/div/input",
            "untis_Email_name")

        # 邮件富文本编辑框
        values = """
                    富文本测试内容:
                        中文：啦啦啦
                        英文：AbcD2*&%￥ sad
                        数字：123456767890
                        特殊符号：<$%#@$()>:;\/\/``~~
                """
        sm.switchFrame("id,unitEdit_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        sm.switchFrame("id,unitEdit1_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()

        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[6]/div/div/div/div/input",
            "Property Details Email Template")
        sm.switchFrame("id,propertyEdit_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        sm.switchFrame("id,propertyEdit1_ifr")
        sm.addText("id,tinymce", values)
        sm.switchFrameOut()
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/div[2]/button"
        )

    @unittest.skip(u"跳过测试！！")
    def test_run_setting(self):
        """setting模块"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Settings")
        # Unit Custom Field Labels
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/div/input",
            "Area Label")
        for i in range(2, 7):
            for a in range(1, 3):
                sm.addText(
                    "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[2]/div[%s]/div[%s]/div/div/div/input"
                    % (i, a), "Custom Field%s-%s" % (i, a))

        # Unit Price Settings
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[1]/div/div/div/div/input",
            "Default Transaction Price Label")
        for i in range(2, 11):
            for a in range(1, 3):
                if a == 1:
                    sm.addText(
                        "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[%s]/div[1]/div/div/div/input"
                        % i, "Price %s Label Text" % i)
                elif a == 2:
                    sm.click(
                        "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[%s]/div[2]/div/div/label"
                        % i)
                else:
                    pass
        # Price Instuction 价格声明内容输入框
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[11]/div[1]/div/div/div/input",
            "“Pricing subject to confirmation")
        #Num of Decimal Places 计算价格时结果保留尾数输入框
        sm.addText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/form/div[4]/div[11]/div[2]/div/div/div/input",
            "2")
        # Selling Entities
        # 清空已添加的公司
        sm.list_del(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[1]",
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[2]/div/button"
        )

        # 添加公司
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[1]/div[2]/button[1]"
        )

        # 选择公司
        # 获取所有已添加的公司名称
        text = sm.getText(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]"
        )
        na = text.strip(",").split("\n")
        for i in na:
            sm.sleeps(0.5)
            sm.list_click(
                "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/div",
                i, "label")
        # 确认勾选
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/button[1]"
        )
        # 保存功能按钮
        sm.click(
            "xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/div[2]/button[1]"
        )
        # 清除功能按钮
        # sm.click("xpath,//*[@id='home']/section/section/main/div/div[2]/div/div[1]/div/div[2]/button[2]")
    @unittest.skip(u"跳过测试！！")
    def test_run_Permissions(self):
        """Permissions模块"""
        sm.list_click(
            "xpath,//*[@id='home']/section/section/main/div/div[1]/ul",
            "Permissions")
