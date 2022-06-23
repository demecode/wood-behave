# Created by demetriswilliams at 23/06/2022
Feature: # As a visitor to the public website,
  # I want to be able to view information about LiveLend
  # so that I understand the company’s background.

  Scenario Outline: # Enter scenario name here
    Given that I visit the LiveLend website
    When I visit the About Us page
    Then I the copy matches the "<copy_ref>"

    Examples:

  Scenario:
    Given that I visit the LiveLend website
    When I visit the About Us page
    Then I am able to click on and navigate to the links displayed in the header