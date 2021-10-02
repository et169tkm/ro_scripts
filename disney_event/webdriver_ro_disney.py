#!/usr/bin/env python3
"""
A script that "shares" the RO Disney event to facebook.

Requires firefox-geckodriver
Requires selenium python library
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import getpass
import sys
import time
from logzero import logger
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def main(args):
  """ Main entry point of the app """
  logger.info(args)

  username = args.username
  if args.stdin_password:
    password = sys.stdin.readline().rstrip()
  else:
    password = getpass.getpass("Facebook password:")
  go(username, password)

def go(username, password):
  
  firefox_profile = webdriver.FirefoxProfile()
  firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
  
  logger.info("Opening browser")
  driver = webdriver.Firefox(firefox_profile=firefox_profile)
  
  ### Open RO page
  logger.info("Opening RO Disney event page (takes a while, be patient)")
  driver.get('https://event.gnjoy.com.tw/RoM/ACT_20210818_Disney#_=_') # takes a while
  WebDriverWait(driver, 180).until(expected_conditions.title_contains("迪士尼聯動"))
  
  ### On the RO page Click login with Facebook
  # driver.find_elements_by_class_name("login__icon--facebook")
  logger.info("Clicking FB button")
  driver.execute_script('TPLogin("FB")')
  
  logger.info("Accepting cookies")
  for i in range(60):
    accept_button_list = driver.find_elements_by_css_selector('button[title="Accept All"]')
    if len(accept_button_list) > 0:
      ActionChains(driver).click(accept_button_list[0]).perform()

  ### On the facebook page, enter username and password
  WebDriverWait(driver, 180).until(expected_conditions.element_to_be_clickable((By.ID, 'email')))

  logger.info("Entering username/password")
  driver.find_element_by_id("email").send_keys(username)
  time.sleep(1)
  driver.find_element_by_id("pass").send_keys(password)
  time.sleep(1)
  driver.find_element_by_id("pass").submit()
  
  ### Back to RO page, run KMS script
  WebDriverWait(driver, 180).until(expected_conditions.title_contains("迪士尼聯動"))
  logger.info("RO event page seems to be loaded")
  logger.info("Injecting KMS script")
  kms_script = """
  // This can be run as soon as jQuery is available, it uses jQuery to wait for document ready
  function runAjax() {
    let share_url = 'ACT_20210818_Disney/sent2';
    let inputData = {
      token: '',
      DateForTest: '',
    };
    window.$(document).ready(function() {
      document.title = "kms_script_document_loaded";
      window.$.ajax({
        async: false,
        type: "POST",
        url: share_url,
        contentType: "application/json; charset=utf-8", // 送出的
        data: JSON.stringify(inputData),
        dataType: "json", // 返回的
        success: function (response) {
          //console.log(response);
          let swal_msg = response;
          if (swal_msg.indexOf("恭禧您獲得") > -1) {
              swal_msg += '</p><span>序號非即時發送，請稍待片刻便可前往 <a target="_blank" href="https://www.gnjoy.com.tw/Coupon/My">序號兌換中心</a> 進行兌換</span>';
          }
          window.swal({ text: swal_msg });
          document.title = "kms_script_ajax_done_succeeded - " + swal_msg;
        },
        error: function (response) {
          console.log(response);
          window.swal({ text: '目前讀取不到資訊，請玩家稍待片刻再操作，謝謝' });
          document.title = "kms_script_ajax_done_failed"
        }
      });
    });
  }
  // Waits for jQuery to become available, then call runAjax()
  function waitForJQuery() {
    console.log("waitForJQuery();");
    if (!!window.$) {
      runAjax();
    } else {
      window.setTimeout(waitForJQuery, 1000);
    }
  }
  waitForJQuery();
  """
  driver.execute_script(kms_script)

  # wait for the ajax to complete (we change the title after the ajax ends)
  WebDriverWait(driver, 180).until(expected_conditions.title_contains("kms_script_document_loaded"))
  logger.info("Document loaded, sending ajax")
  WebDriverWait(driver, 180).until(expected_conditions.title_contains("kms_script_ajax_done"))
  page_title = driver.title
  if "kms_script_ajax_done_succeeded" in page_title:
    logger.info("ajax resposne: " + page_title)
    logger.info("ajax succeeded, going to close browser in 5 seconds")
    time.sleep(5)
    driver.close()
  else:
    logger.warning("ajax failed, keeping the browser open")
    


if __name__ == "__main__":
  """ This is executed when run from the command line """
  parser = argparse.ArgumentParser()

  # Required positional argument
  parser.add_argument("username", help="Required facebook username (email)", action="store")

  # Optional argument flag which defaults to False
  parser.add_argument("-p", "--stdin_password", action="store_true", default=False, help="Read password from stdin instead of prompting for input")

  # Optional argument which requires a parameter (eg. -d test)
  #parser.add_argument("-n", "--name", action="store", dest="name")

  # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
  parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0,
    help="Verbosity (-v, -vv, etc)")

  # Specify output of "--version"
  parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s (version {version})".format(version=__version__))

  args = parser.parse_args()
  main(args)

