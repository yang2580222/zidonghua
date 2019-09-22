from test_case.conftest import driver


def test_login(driver):
    driver.get("打开浏览器","http://ui.yansl.com/#/input")
    driver.click("点击表单元素","(//div[@class ='el-submenu__title'])[1]")
    driver.click("点击输入框","""//li[text()="输入框(7)"]""")
    driver.send_keys("在纯输入框中输入","""//input[@name="t1"]""","中午好，杨云飞")
    driver.send_keys("在纯密码框中输入","""//input[@name="t2"]""","ab123456")
    driver.send_keys("在纯文本框中输入","""//textarea[@name="t3"]""","你是最高棒的")
    driver.send_keys("在输入框2中输入", """//input[@name="t4"]""", "你的名字，我的姓氏")
    driver.send_keys("在密码框2中输入", """//input[@name="t5"]""", "傅风眠")
    driver.send_keys("在文本域2中输入", """//textarea[@name="t6"]""", "傅风眠")
    driver.send_keys("在建议框1中输入", """//input[@name="t7"]""", "傅风眠")
    driver.send_keys("在建议框2中输入", """//input[@name="t8"]""", "傅风眠")
    driver.click("点击数据处理","""(//div[@class="el-submenu__title"])[2]""")
    driver.click("点击表格(9)", """//li[text()="表格(9)"]""")












if __name__ == '__main__':
    test_login(driver)
