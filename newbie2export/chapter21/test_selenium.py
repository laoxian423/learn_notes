# LOOK selenium and geckodriver 
"""
   用 selenium 操作 firfox 浏览器打开页面，抓取动态数据
   解决版本兼容问题 https://github.com/mozilla/geckodriver/releases
   不需要安装，解压即可。
   在windows环境变量中增加firefox 和 geckodriver的路径
"""
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://q.stock.sohu.com/cn/600992/cjmx.shtml')
em = driver.find_element_by_id('BIZ_IS_dealdetail_l')
print(em.text)
driver.quit()
