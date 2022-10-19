#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 18th, 2022
# This program asks the user for their age
# It then displays if they can date my grandchild
import constants


def main():
    # this function tells you if you can date my grandchild
    # declare a variable that represents the users age
    user_age_string = input("Enter your age: ")
    # use a try catch to ensure user properly enters their age
    try:
        # convert string variable to int
        user_age_string = int(user_age_string)
        # check if the user is able to date my grandchild
        if user_age_string > constants.MIN_AGE and user_age_string < constants.MAX_AGE:
            # if the user can, tell them
            print("You can date my grandchild.")
        else:
            # if the user can't, tell them
            print("You cannot date my grandchildren.")
    # tell the user they incorrectly inputted their age
    except Exception:
        print("You did not properly enter an age.")
    finally:
        # display following regardless of error or not
        print("Thank you for being interested in my grandchild.")


if __name__ == "__main__":
    main()
