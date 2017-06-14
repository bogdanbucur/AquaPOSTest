import os
import unittest
from time import sleep
from random import randint

from appium.webdriver import webelement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium import webdriver


class AquaPOS(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'Samsung',
            'app': 'C:/Users/bogda/PycharmProjects/AquaPOS/src/AquaPOS.apk',
            'appPackage': 'com.udev.alidemirel.aquapos',
            'appActivity': 'activities.Register'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # def test_1(self):
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/codeText').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id'
    #                                    '/codeText').send_keys('ebf58e09-84bb-37d3-b4d0-e7fc2ea270e1')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnRegister').click()

    # def test_2(self):
    #     self.driver.find_element_by_name('User Carrefour 2').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').send_keys('0000')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnLogin').click()

    def test_3(self):
        sleep(2)
        self.driver.find_element_by_name('User Carrefour 2').click()
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').click()
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').send_keys('0000')
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnLogin').click()

        for i in range(3):
            self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout'
                                              '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, {0})]'.format(str(i))).click()
            sleep(2)
            products = randint(1, 5)
            for j in range(products):
                self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout'
                                                  '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, {0})]'.format(str(j))).click()

            self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnBackToCategories').click()

        # cart_len = self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/cartListSize').get_attribute('text')
        # for k in range(int(cart_len)):
        #     product = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
        #                                                 '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, {0})]'.format(str(k)))
        #     quantity = randint(1, 10)
        #     for l in range(quantity):
        #         product.find_element_by_id('com.udev.alidemirel.aquapos:id/addProduct').click()
        #
        # self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnCheckout').click()
        # self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnPaymentCash').click()
        # sleep(2)
        # price = self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/viewTotalPrice').get_attribute('text')
        # self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enteredValue').send_keys(price)
        # self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnCompleteOrder').click()
        sleep(2)

        product = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                    '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, {0})]'.format(str(2)))
        product.find_element_by_id('com.udev.alidemirel.aquapos:id/addProduct').click()


        sleep(2)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AquaPOS)
    unittest.TextTestRunner(verbosity=2).run(suite)