Feature: Setup page
    As an admin
    I want to create an initial admin account
    so that I can start using this thing.

    @local
    Scenario Outline: Creating an admin account
        Given there's no admin account
        When I go to /setup
        And I enter <username>, <password>, and <email>
        Then I should be logged in as <username>

        Examples: Users
            | username | password | email         |
            | friend   | hello    | wow@great.com |
