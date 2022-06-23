# Created by demetriswilliams at 23/06/2022
Feature: # As a Visitor to the public website
  # I want to be able to view information about LiveLend interest nd amount repayable using the calculator
  # So that I can know about loan cost and affordability

  Scenario Outline: Borrow Amount
    Given that I am on the LiveLend website homepage
    When I move the 'borrow amount' slider from between <amount_one> to <amount_two>
    Then the <monthly_repayment> AND <total_amount> Repayable figures will change to the correct amounts

    Examples:
      | amount_one | amount_two | monthly_repayment | total_amount |
      | 12000      | 1000       | 433.72            | 18,216.17    |

  Scenario Outline: # Enter scenario name here
    Given that I am on the LiveLend website homepage
    When I move the 'loan term' slider from between <amount_one> to <amount_two>
    Then the Monthly Repayment AND Total Amount Repayable figures will change to the correct amounts

    Examples:
      | amount_one | amount_two |
      | 1000       | 16000      |

  Scenario Outline: # Enter scenario name here
    Given that I am on the LiveLend website homepage
    When I click on the 'Get my Quote' button
    Then I am redirected straight to the <main> url

    Examples:

      | main                 |
      | https://livelend.co/ |



