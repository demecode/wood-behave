from behave import *
from utils.endpoints import *
from locators.home_page import *
from selenium.webdriver import ActionChains
from utils.stripd import only_numbers
import time
import re
import string

use_step_matcher("re")


@given("that I am on the LiveLend website homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.helperfunc.open(BASEURL + LIVE_STAGING)
    context.helperfunc.maximize()
    context.helperfunc.find_by_xpath(accept_terms_button_xpath).click()


@when('I move the \'borrow amount\' slider from between "<>" to "<>"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I move the \'borrow amount\' slider from between "<>" to "<>"')


@then("the Monthly Repayment AND Total Amount Repayable figures will chang to the correct amounts")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then the Monthly Repayment AND Total Amount Repayable figures will chang to the correct amounts')


@then("the Monthly Repayment AND Total Amount Repayable figures will change to the correct amounts")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then the Monthly Repayment AND Total Amount Repayable figures will change to the correct amounts')


@when("I click on the 'Get my Quote' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I click on the \'Get my Quote\' button')


@then('I am redirected straight to the "<>" url')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I am redirected straight to the "<>" url')


@when("I move the 'borrow amount' slider from between <> to <>")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I move the \'borrow amount\' slider from between <> to <>')


@when("I move the 'loan term' slider from between <> to <>")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I move the \'loan term\' slider from between <> to <>')


@then("I am redirected straight to the <> url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I am redirected straight to the <> url')


@when("I move the 'borrow amount' slider from between (?P<amount_one>.+) to (?P<amount_two>.+)")
def step_impl(context, amount_one, amount_two):
    """
    :type context: behave.runner.Context
    :type amount_one: str
    :type amount_two: str
    """
    context.helperfunc.find_by_id(loan_amount_slider_id).clear()
    loan_slider = context.helperfunc.find_by_id(loan_amount_slider_id)
    time.sleep(2)
    ActionChains(context.helperfunc._driver).click_and_hold(loan_slider).pause(1).move_by_offset(140,
                                                                                                 0).release().perform()
    loan_amount_slider_1 = context.helperfunc.find_by_xpath(loan_amount_slider_text).text

    new_loan_amount_slider_1 = only_numbers(loan_amount_slider_1)
    assert amount_one == new_loan_amount_slider_1


@when("I move the 'loan term' slider from between (?P<amount_one>.+) to (?P<amount_two>.+)")
def step_impl(context, amount_one, amount_two):
    """
    :type context: behave.runner.Context
    :type amount_one: str
    :type amount_two: str
    """

    raise NotImplementedError(u'STEP: When I move the \'loan term\' slider from between <amount_one> to <amount_two>')


@then("I am redirected straight to the (?P<main>.+) url")
def step_impl(context, main):
    """
    :type context: behave.runner.Context
    :type main: str
    """
    raise NotImplementedError(u'STEP: Then I am redirected straight to the <main> url')


@then("the (?P<monthly_repayment>.+) AND (?P<total_amount>.+) Repayable figures will change to the correct amounts")
def step_impl(context, monthly_repayment, total_amount):
    """
    :type context: behave.runner.Context
    :type monthly_repayment: str
    :type total_amount: str
    """
    monthly_returned_from_web_page = only_numbers(context.helperfunc.find_by_id(monthly_repayment_id).text)
    total_return_from_web_page = only_numbers(context.helperfunc.find_by_id(total_repayment_amount_id).text)
    r_monthly_repayment = only_numbers(monthly_repayment)
    r_total_amount = only_numbers(total_amount)

    #
    assert r_monthly_repayment == monthly_returned_from_web_page
    assert r_total_amount == total_return_from_web_page
