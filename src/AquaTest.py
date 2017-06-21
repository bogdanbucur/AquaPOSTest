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
            'app': 'C:\Users\BogdanBucur\PycharmProjects\AquaPOSTest\src\AquaPOS1.apk',
            'appPackage': 'com.udev.alidemirel.aquapos',
            'appActivity': 'activities.Register'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # # Register Device
    # def test_1(self):
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/codeText').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/codeText').send_keys("ebf58e09-84bb-37d3-b4d0-e7fc2ea270e1")
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnRegister').click()
    # #
    #
    # # User Login
    # def test_2(self):
    #     sleep(2)
    #     self.driver.find_element_by_name('User Carrefour 2').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').send_keys('0000')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnLogin').click()

    # Create Order with Cash Checkout
    # def test_3(self):
    #     sleep(2)
    #     self.driver.find_element_by_name('User Carrefour 2').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').send_keys('0000')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnLogin').click()
    #     sleep(2)
    #
    # # Find the number of categories
    #     category_list = self.driver.find_elements_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout'
    #                                                        '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
    #
    #     for i in range(len(category_list)):
    #         # Enter each category 1 by 1
    #         self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout'
    #                                           '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "{0}")]'.format(str(i))).click()
    #         # Find the number of products
    #         product_list = self.driver.find_elements_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
    #                                                           '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
    #         rand_products = randint(1, len(product_list))
    #
    #         list = []
    #
    #         # Place a random number of products in the shopping cart
    #         for j in range(rand_products):
    #             rand_product = randint(1, len(product_list)) - 1
    #             product = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout'
    #                                                         '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "{0}")]'.format(str(rand_product)))
    #             product_name = product.find_element_by_id('com.udev.alidemirel.aquapos:id/itemName').get_attribute('text')
    #             if product_name not in list:
    #                 list.append(product_name)
    #                 product.click()
    #
    #         self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnBackToCategories').click()
    #         sleep(2)
    #
    #     # Scroll to the beginning of the Shopping Cart list
    #     k = True
    #     while k:
    #         el1_aux = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                     '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "0")]')
    #         el1_aux_name = el1_aux.find_element_by_id('com.udev.alidemirel.aquapos:id/productName').get_attribute('text')
    #
    #         self.driver.scroll(
    #             self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                               '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "0")]'),
    #             self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                               '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "2")]')
    #         )
    #
    #         el1 = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
    #                                                 '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "0")]')
    #         el1_name = el1.find_element_by_id('com.udev.alidemirel.aquapos:id/productName').get_attribute('text')
    #
    #         el1_aux = el1
    #
    #         # Verify if the old first element is the same as the new first element
    #         if el1_name != el1_aux_name:
    #             self.driver.scroll(
    #                 self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                   '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "0")]'),
    #                 self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                   '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "2")]')
    #             )
    #
    #         else:
    #             k = False
    #
    #     cart_list = self.driver.find_elements_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                    '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
    #     cart_size = int(self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/cartListSize').get_attribute('text'))
    #
    #     # Increasing quantity while scrolling the list
    #     if len(cart_list) >= cart_size:
    #         for l in range(len(cart_list)):
    #             quantity = randint(1, 10)
    #             cart_product = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                              '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "{0}")]'.format(str(l)))
    #             for m in range(quantity):
    #
    #                 cart_product.find_element_by_id('com.udev.alidemirel.aquapos:id/addProduct').click()
    #
    #     else:
    #         o = 0
    #         for n in range(cart_size):
    #             quantity = randint(1, 10)
    #             cart_product = self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                              '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "{0}")]'.format(str(n - o)))
    #             for m in range(quantity):
    #                 cart_product.find_element_by_id('com.udev.alidemirel.aquapos:id/addProduct').click()
    #
    #             if n >= (len(cart_list) - 1):
    #                 self.driver.scroll(
    #                     self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                       '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "{0}")]'.format(len(cart_list) - 1)),
    #                     self.driver.find_element_by_xpath('//android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
    #                                                       '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[contains(@index, "{0}")]'.format(len(cart_list) - 2))
    #                 )
    #                 o = o + 1
    #
    #     # Checkout
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnCheckout').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnPaymentCash').click()
    #     price = self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/viewTotalPrice').get_attribute('text')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enteredValue').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enteredValue').send_keys(price)
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnCompleteOrder').click()

    # Create Advance Payment
    # def test_4(self):
    #     sleep(2
    #           )
    #     self.driver.find_element_by_name('User Carrefour 2').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').send_keys('0000')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnLogin').click()
    #
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnFilter').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnAdvancePay').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enteredAdvance').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enteredAdvance').send_keys('100')
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/avansDesc').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/avansDesc').send_keys('Advance Payment')
    #     chance = randint(1, 2)
    #     if chance == 1:
    #         self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnCash').click()
    #     else:
    #         self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnCard').click()
    #     self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnSubmit').click()

    # Make a Refund on a Random Order
    def test_5(self):
        sleep(2)
        self.driver.find_element_by_name('User Carrefour 2').click()
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').click()
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/userPin').send_keys('0000')
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnLogin').click()
        sleep(3)

        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnFilter').click()
        self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnSales').click()
        sleep(2)

        orderIndex = randint(1, 5)
        order = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[contains(@index, "1")]'
                                                  '/android.widget.LinearLayout[contains(@index, "0")]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout'
                                                  '[contains(@index, "{0}")]'.format(orderIndex))
        order.click()

        orderType = order.find_element_by_id('com.udev.alidemirel.aquapos:id/orderType').get_attribute('text')
        if orderType == 'order':
            self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnRefund').click()
            sleep(1)
            orderProductList = self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout')
            k = 0
            for i in range(len(orderProductList)):
                orderProduct = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                                                                 '/android.widget.LinearLayout[contains(@index, "{0}")]'.format(i - k))

                if int(orderProduct.find_element_by_id('com.udev.alidemirel.aquapos:id/productQuantity').get_attribute('text')) > 0:
                    orderProductQuantity = int(orderProduct.find_element_by_id('com.udev.alidemirel.aquapos:id/productQuantity').get_attribute('text'))
                    randomQuantity = randint(1, orderProductQuantity)
                    self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enterQuantity').click()
                    self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/enterQuantity').send_keys(randomQuantity)

                # if i == len(orderProductList) - 1:
                #     self.driver.scroll(
                #         self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                #                                            '/android.widget.LinearLayout[contains(@index, "{0}")]'.format(len(orderProductList) - 2)),
                #         self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                #                                            '/android.widget.LinearLayout[contains(@index, "{0}")]'.format(len(orderProductList) - 3))
                #     )
                #     k = k + 1

            sleep(2)
            self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/textRefundDesc').click()
            self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/textRefundDesc').send_keys('Pleb wants refund...')
            self.driver.find_element_by_id('com.udev.alidemirel.aquapos:id/bttnRefund').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AquaPOS)
    unittest.TextTestRunner(verbosity=2).run(suite)
