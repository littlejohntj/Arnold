from __future__ import print_function
from auth import Twitter_Auth, Reddit_Auth, Instagram_Auth
from twitter_module import *
from reddit_module import *


# Have some sort of user menu to let the user pick which accounts
# they want to authorize.
class Arnold():
    print("Welcome to Arnold, your top social media feeds all in one place!")

    def menu(self):
        print("What would you like to do:")
        print("\t1.Add an account.")
        print("\t2.View your aggregate feed.")
        print("\t3.View a single feed.")
        input = raw_input("Please select a number: ")
        if input != 1 or input != 2 or input != 3:
            print("Invalid input!")
            self.menu()
        else:
            return self.second_menu(input)
    
    def second_menu(self, input):
        if input == 1:
            print("Which social media account would you like to add: ")
            print("\t1.Reddit")
            print("\t2.Instagram")
            print("\t3.Twitter")
            input = raw_input("Please select a number: ")
            if input == 1:
                self.add_reddit_account()
            if input == 2:
                self.add_instagram_account()
            if input == 3:
                self.add_twitter_account()
            else:
                print("Invalid input!")
                self.second_menu(1)
        elif input == 2:
            # print aggregate feed here
            self.get_reddit()
            self.get_instagram()
            self.get_twitter()
            self.menu()
        elif input == 3:
            print("Which feed would you like to view: ")
            print("\t1.Reddit")
            print("\t2.Instagram")
            print("\t3.Twitter")
            input = raw_input("Please select a number: ")
            if input != 1 or input != 2 or input != 3:
                print("Invalid input!")
                self.second_menu(3)
            else:
                self.get_single_timeline(input)
                self.menu()

    # Twitter Authorization
    # _twitter = Twitter_Auth()
    # twitter_api = _twitter.get_authorized_user()
    def add_twitter_account(self):
        self.twitter_api = Twitter_Auth().get_authorized_user()


    # Instagram Authorization
    # _instagram = Instagram_Auth()
    # instagram_api = _instagram.get_authorized_user()
    def add_instagram_account(self):
        self.instagram_api = Instagram_Auth().get_authorized_user()


    # Reddit Authorization
    # _reddit = Reddit_Auth()
    # reddit_api = _reddit.get_authorized_user()
    def add_reddit_account(self):
        self.reddit_api = Reddit_Auth().get_authorized_user()


    # Call get_timeline(twitter_api) to get the users twitter timeline
    def get_twitter(self):
        get_timeline(self.twitter_api)


    # Call TJs function to display user feed and pass instagram_api as a parameter
    def get_instagram(self):
        # TJ's call?
        5+2

    # Call katies print_timeline(reddit_api) to display users reddit timeline
    def get_reddit(self):
        print_timeline(self.reddit_api)


    def get_single_timeline(self, choice):
        if choice == 2:
            self.get_instagram()
        elif choice == 1:
            self.get_reddit()
        elif choice == 3:
            self.get_twitter()
        self.menu()


if __name__ == "__main__":
    Arnold()
