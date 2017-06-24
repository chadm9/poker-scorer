

read_in = open('hand.txt', 'r')
input = read_in.readlines()

# print input

def get_hand(stryng):
    hand = stryng.split(' ')
    hand[-1] = hand[-1].replace('\n', '')
    player_1_hand = hand[0:5]
    player_2_hand = hand[5:10]
    hands = []
    hands.append(player_1_hand)
    hands.append(player_2_hand)


    return hands

# print get_hand(input[0])




# flushes have all the same suit (which appears at index -1 of the card string.  This function checks for a flush)

def has_flush(hand):
    suit = hand[0][-1]
    for cards in hand:
        if cards[-1] == suit:
            pass
        else:
            return False

    return True

def convert_to_int(stryng):
    dyct = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

    if dyct.has_key(stryng):
        return int(dyct[stryng])
    else:
        return int(stryng)



def has_straight(hand):

    previous_number = convert_to_int(hand[0][0:-1])
    this_number = None

    for i in range(1, len(hand)):
        this_number = convert_to_int(hand[i][0:-1])

        if not (this_number == previous_number + 1 ):
            return False

        previous_number = convert_to_int(hand[i][0:-1])

    return True




def has_duplicates(hand):
    duplicate_cards = 1
    max_duplicates = 1
    max_card_value = 0
    secondary_duplicate = 0
    highest_card_in_hand = 0

    for i in range(len(hand)-1):
        current_card_value = convert_to_int(hand[i][0])
        j = i + 1
        # print current_card_value
        while j < (len(hand)):



            if hand[i][0] == hand[j][0]:
                duplicate_cards += 1

                if max_duplicates <= duplicate_cards:
                    max_duplicates = duplicate_cards

                    if current_card_value > max_card_value:
                        secondary_duplicate = max_card_value
                        max_card_value = current_card_value


                # elif duplicate_cards == 2:
                #     secondary_duplicate = current_card_value



            j += 1



        duplicate_cards = 1


    return [max_duplicates, max_card_value, secondary_duplicate]


def highest_card(hand):
    highest_card_value = 0
    for i in range(len(hand)):
        current_card_value = convert_to_int(hand[i][0])

        if current_card_value > highest_card_value:
            highest_card_value = current_card_value

    return highest_card_value


# test_hand = ['2C', 'KS', 'KC', 'KS', '2D']
#
# print has_duplicates(test_hand)

# print highest_card(test_hand)

def hand_strength(hand):

    if has_flush(hand) and has_straight(hand):
        return[10, highest_card(hand)]
    elif has_flush(hand):
        return [9, highest_card(hand)]
    elif has_duplicates(hand)[0]==4:
        return [8, has_duplicates(hand)[1]]
    elif has_duplicates(hand)[0]==3 and has_duplicates(hand)[2] != 0:
        return [7, has_duplicates(hand)[1]]
    elif has_straight(hand):
        return [6, highest_card(hand)]
    elif has_duplicates(hand)[0]==3:
        return [5, has_duplicates(hand)[1]]
    elif has_duplicates(hand)[0]==2 and has_duplicates(hand)[2] != 0:
        return [4, has_duplicates(hand)[1], has_duplicates(hand)[2]]
    elif has_duplicates(hand)[0]==2:
        return [3, has_duplicates(hand)[1], highest_card(hand)]
    else:
        return [2, highest_card(hand)]



# print hand_strength(test_hand)

player1wins = 0
player2wins = 0

for hands in input:




    hand1 = get_hand(hands)[0]
    hand2 = get_hand(hands)[1]

    hand1strength = hand_strength(hand1)
    hand2strength = hand_strength(hand2)



    if hand1strength[0] != hand2strength[0]:
        if hand1strength[0] > hand2strength[0]:
            player1wins +=1
        else:
            player2wins +=1

    # elif len(hand1strength) != len(hand2strength):
    #     if len(hand1strength) > len(hand2strength):
    #         player1wins +=1
    #     else:
    #         player2wins +=1

    elif hand1strength[1] != hand2strength[1]:
        if hand1strength[1] > hand2strength[1]:
            player1wins += 1
        else:
            player2wins += 1

    elif hand1strength[2] != hand2strength[2]:
        if hand1strength[2] > hand2strength[2]:
            player1wins += 1
        else:
            player2wins += 1

    # print hand_strength(hand1), hand_strength(hand2)

print 'player 1 wins: ' + str(player1wins) + '\nplayer 2 wins: ' + str(player2wins)

