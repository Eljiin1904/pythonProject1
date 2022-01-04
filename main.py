import requests
# import libaries

# Selenium Web Driver
from selenium import webdriver


# Site status validation
r = requests.get("http://deckofcardsapi.com/")
# Api status
print("Card deck status code:", r.status_code)
assert r.status_code == 200


# Test Platform Intro
def start_testing():
    print("\nSection 1.1: New Deck Functionality \n")


def dont_test():
    print("\nOk, Start testing when ready.\n")


print("\nWelcome to the Card Deck validation platform! ")
print("\nDuring this test run, we will validate the functionality of the card deck game API")

choice = ''
while choice != 'q':
    print("\n[1] Start testing Section 1.1")
    print("[2] Test Failed, Pause testing")
    print("[q] Quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        start_testing()
        break


    elif choice == '2':
        dont_test()


    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    else:
        print("\nI don't understand that choice, please try again.\n")
        break


# New Desk section
def dont_test1():
    print("\nOk, Start testing when ready.\n")


def new_deck():
    print("\n")
    print("Test Scenario 1.2: Validate the API/URL response has a new unique ID for DECK_ID value. Also validate the REMAINING value is equal to 52\n")


print("Test 1.1 Description: Validate the data response from a newly created deck")

choice = ''
while choice != 'q' or '1':
    print("\n[1] Start test and create new deck")
    print("[2] Don't start testing")
    print("[q] Enter q to quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        new_deck()
        break

    elif choice == '2':
        dont_test1()



    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    else:

        break



print("Expected sample response below:")
print("{success: true, deck_id: 3o39hangitfc, remaining: 52, shuffled: true}")
newdeck = requests.get("http://deckofcardsapi.com/api/deck/new/?deck_count=1")
print("\nTest API response below:")
print(newdeck.text)


def dont_test2():
    print("\nOk, Start testing when ready\n")


def new_deck2():
    print("\nSection 1.2: Draw Card Functionality\n")


print("\nNote:For the 1.2 test, the value of the new DECK_ID must be passed to drawcards URL in the source code.")
print("Quit out (q) of test run to pass DECK_ID to drawcards URLs. Update code ines 170-174")


choice = ''
while choice != 'q' or '1':
    print("\n[1] Test Passed, Continue testing")
    print("[2] Test Failed, Pause testing")
    print("[q] Test Failed, Quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        new_deck()
        break
    elif choice == '2':
        dont_test1()


    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    else:
        print("\nI don't understand that choice, please try again.\n")
        break



# Draw cards from deck

def draw_card():
    print("\nTest Scenario 1.2: Validate the API/URL response draws five random cars. Also vaildate (take note) of the first delt card. The card id will be passed in the URL for test case 1.3. Line 232. Finally validate the card count is 37 \n")
    print("1.3 URL example: http//deckofcardsapi.com/api/deck/DECK_ID VALUE/return/?cards=(UPDATE VALUE WITH FIRST CARD DEALT")


def dont_test3():
    print("\nOk, Start testing when ready\n")


print("Test Description 1.2: Validate a successful response returns the correct amount of requested drawn cards.")

choice = ''
while choice != 'q' or '1':
    print("\n[1] Start Test, Draw card from deck")
    print("[2] Dont start testing")
    print("[q] Enter q to quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        draw_card()
        break
    elif choice == '2':
        dont_test2()


    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    else:
        print("\nI don't understand that choice, please try again.\n")
        break

print("Sample response below:")
print("{success: true, deck_id: 7li5jp2q2dky, cards: [{code: 2S, image: https//deckofcardsapi.com/static/img/2S.png, images: {svg: https//deckofcardsapi.com/static/img/2S.svg, png: https//deckofcardsapi.com/static/img/2S.png}, value: 2, suit: SPADES}], remaining: 52}")
drawcards = requests.get("http://deckofcardsapi.com/api/deck/we4vetqlkmwk/draw/?count=5")
drawcards = requests.get("http://deckofcardsapi.com/api/deck/we4vetqlkmwk/draw/?count=4")
drawcards = requests.get("http://deckofcardsapi.com/api/deck/we4vetqlkmwk/draw/?count=3")
drawcards = requests.get("http://deckofcardsapi.com/api/deck/we4vetqlkmwk/draw/?count=2")
drawcards = requests.get("http://deckofcardsapi.com/api/deck/we4vetqlkmwk/draw/?count=1")
print("\nTest API response below:")
print(drawcards.text)


# Return card to deck
def return_card():
    print("\nSection 1.3: Return Card Functionality")


def dont_test4():
    print("\nOk, Start testing when ready\n")


choice = ''
while choice != 'q' or '1':
    print("\n[1] Test Passed, Continue testing")
    print("[2] Test Failed, Pause testing")
    print("[q] Test Failed, Quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        return_card()
        break
    elif choice == '2':
        dont_test3()

    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    else:
        print("\nI don't understand that choice, please try again.\n")
        break


# Verify Deck Count

def verify_card():
    print(
        "\nTest Scenario 1.3: Validate the API/URL response returns the first drawn card back to the deck. Finally validate correct amount of cards (48) is returned to the deck\n")


def dont_test5():
    print("\nOk, Start testing when ready\n")


print("\nTest Description 1.3: Validate the first drawn card is returned back to the deck")

choice = ''
while choice != 'q' or '1':
    print("\n[1] Start Testing, Return cards to the deck")
    print("[2] Don't start test")
    print("[q] Enter q to quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        verify_card()
        break
    elif choice == '2':
        dont_test4()

    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    else:
        print("\nI don't understand that choice, please try again.\n")
        break

print("Sample response below:")
print("http//deckofcardsapi.com/api/deck/DECK_ID VALUE/return/?cards=JC\n")
print("Expected API response below:")
returncard = requests.get("http://deckofcardsapi.com/api/deck/iisz956v90c6/return/?cards=KS")
print(returncard.text)
print("\nValidation for returned card amount below:")
returncard2 = requests.get("http://deckofcardsapi.com/api/deck/29prdyj0stkx/?list")
print(returncard2.text)


def return_card2():
    print("\nEnd of test message\n")


def dont_test5():
    print("\nOk, Start testing when ready\n")


choice = ''
while choice != 'q' or '1':
    print("\n[1] Test Passed, End test run")
    print("[2] Test Failed, End test run")
    print("[q] Quit testing")

    choice = input("\nWhat would you like to do? ")
    if choice == '1':
        return_card()
        break
    elif choice == '2':
        dont_test3()

    elif choice == 'q':
        print("\nQuiting test run.\n")
        quit()

    elif choice == '':
        print("\nI don't understand that choice, please try again.\n")
        break


    else:
        print("\nI don't understand that choice, please try again.\n")


print("Test Case 1.1: New Deck Passed")
print("Test Case 1.2: Draw Card Passed")
print("Test Case 1.3: Return Card Passed ")
