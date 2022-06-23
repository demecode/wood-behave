# Created by demetriswilliams at 23/06/2022
Feature: # As a Visitor to the public website
  # I want to be able to view information about LiveLend interest nd amount repayable using the calculator
  # So that I can know about loan cost and affordability

  Scenario Outline: # Enter scenario name here
    Given that I am on the LiveLend website homepage
    When I move the 'borrow amount' slider from between "<>" to "<>"
    Then the Monthly Repayment AND Total Amount Repayable figures will chang to the correct amounts

    Examples:

  Scenario Outline: # Enter scenario name here
    Given that I am on the LiveLend website homepage
    When I move the 'loan term' slider from between "<>" to "<>"
    Then the Monthly Repayment AND Total Amount Repayable figures will change to the correct amounts

    Examples:

  Scenario Outline:
    Given that I am on the LiveLend website homepage
    When I click on the 'Get my Quote' button
    Then I am redirected straight to the "<>" url

    Examples:



