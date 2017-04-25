from __future__ import print_function
from auth import Twitter_Auth, Reddit_Auth, Instagram_Auth
from twitter_module import *
from reddit_module import *
from instagram_module import *

# Have some sort of user menu to let the user pick which accounts
# they want to authorize.
class Arnold():
    print("Welcome to Arnold, your top social media feeds all in one place!")
    print("----------------------------------------------------------------")


    def __init__(self):
        self.instagramAuthed=False
        self.redditAuthed=False
        self.twitterAuthed=False
        
    def menu(self):
        print("")
        print("What would you like to do:")
        print("\t1.Add an account.")
        print("\t2.View your aggregate feed.")
        print("\t3.View a single feed.")
        print("\t4.Quit.")
        input = raw_input("Please select a number: ")
        print("")
        input=int(input)
        if input == 1 or input == 2 or input == 3:
            self.second_menu(input)
        elif input == 4:

            print("Goodbye!")
            quit()
        else:
            print("----------------------")
            print("Invalid input!")
            print("----------------------")
            self.menu()
    
    def second_menu(self, input):
        if input == 1:
            #Adding a single social media account
            print("Which social media account would you like to add: ")
            print("\t1.Reddit")
            print("\t2.Instagram")
            print("\t3.Twitter")
            input = raw_input("Please select a number: ")
            print("")
            input=int(input)
            if input == 1:
                self.add_reddit_account() #Assuming there's error checking in here to make sure an authenticated account is always returned
                self.redditAuthed=True
                self.menu()
            if input == 2:
                self.add_instagram_account()
                self.instagramAuthed = True
                self.menu()
            if input == 3:
                self.add_twitter_account()
                self.twitterAuthed = True
                self.menu()
            else:
                print("----------------------")
                print("Invalid input!")
                print("----------------------")
                self.second_menu(1)
        elif input == 2:
            # print aggregate feed here
            if not self.twitterAuthed and not self.redditAuthed and not self.instagramAuthed:

                print(" --------------------------------------------------------------------------")
                print("| Please authenticate an account if you'd like to see your aggregate feed. |")
                print(" --------------------------------------------------------------------------")
                print("")
                self.second_menu(1)
            if self.twitterAuthed:
                self.get_twitter()
            if self.redditAuthed:
                self.get_reddit()
            if self.instagramAuthed:
                self.get_instagram()
            self.menu()
        elif input == 3:
            #getting feed for single social media
            print("Which feed would you like to view: ")
            print("\t1.Reddit")
            print("\t2.Instagram")
            print("\t3.Twitter")
            input = raw_input("Please select a number: ")
            print("")
            input=int(input)
            if input != 1 and input != 2 and input != 3:
                print("----------------------")
                print("Invalid input!")
                print("----------------------")
                print("")
                self.second_menu(3)
            elif not self.twitterAuthed and not self.redditAuthed and not self.instagramAuthed:
                print(" -------------------------------------------------------------------------- ")
                print("| Please authenticate an account if you'd like to see your aggregate feed. |")
                print(" -------------------------------------------------------------------------- ")
                print("")
                self.second_menu(1)
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
        print("")


    # Call TJs function to display user feed and pass instagram_api as a parameter
    def get_instagram(self):
        get_recent_posts(self.instagram_api)
        print("")

    # Call katies print_timeline(reddit_api) to display users reddit timeline
    def get_reddit(self):
        print_timeline(self.reddit_api)
        print("")


    def get_single_timeline(self, choice):
        if choice == 2:
            self.get_instagram()
        elif choice == 1:
            self.get_reddit()
        elif choice == 3:
            self.get_twitter()



if __name__ == "__main__":
    prog=Arnold()
    prog.menu()
    
