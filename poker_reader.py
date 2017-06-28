

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
    player_hand = []

    for i in range(len(hand)):
        player_hand.append(convert_to_int(hand[i][0:-1]))

    player_hand = sorted(player_hand)


    previous_number = player_hand[0]

    for i in range(1, len(player_hand)):
        this_number = player_hand[i]

        if not (this_number == previous_number + 1 ):
            return False

        previous_number = player_hand[i]

    return True

def get_hand_value_array(hand):

    player_hand = []

    for i in range(len(hand)):
        player_hand.append(convert_to_int(hand[i][0:-1]))

    player_hand = sorted(player_hand)
    player_hand.reverse()

    return player_hand



def hand_dictionary(hand):
    hand_dict = {}
    for i in range(len(hand)):
        if not hand_dict.has_key(convert_to_int(hand[i][0])):
            hand_dict[convert_to_int(hand[i][0])] = 1
        else:
            hand_dict[convert_to_int(hand[i][0])] += 1
    return hand_dict

def has_full_house(hand):
    hand_dict = hand_dictionary(hand)
    #print hand_dict
    has_pair = None
    has_triple = None
    for key in hand_dict:

        if hand_dict[key] == 2:
            has_pair = True
        if hand_dict[key] == 3:
            has_triple = True


    return has_pair and has_triple
    # if has_pair and has_triple:
    #     return True
    # else:
    #     return False


def has_4_of_a_kind(hand):
    hand_dict = hand_dictionary(hand)
    #print hand_dict
    has_quads = None

    for key in hand_dict:

        if hand_dict[key] == 4:
            return True

    return False

def has_3_of_a_kind(hand):
    hand_dict = hand_dictionary(hand)


    for key in hand_dict:

        if hand_dict[key] == 3:
            return True

    return False

def has_2_pair(hand):
    hand_dict = hand_dictionary(hand)
    number_of_pairs = 0
    for key in hand_dict:

        if hand_dict[key] == 2:
            number_of_pairs += 1

    if number_of_pairs ==2 :
        return True
    else:
        return False


def has_pair(hand):
    hand_dict = hand_dictionary(hand)
    number_of_pairs = 0
    for key in hand_dict:

        if hand_dict[key] == 2:
            number_of_pairs += 1

    if number_of_pairs ==1 :
        return True
    else:
        return False

def which_pair(hand):
    hand_dict = hand_dictionary(hand)

    pair_value = None
    for key in hand_dict:

        if hand_dict[key] == 2:
            #print key
            pair_value = key


    return pair_value


def which_2_pair(hand):
    hand_dict = hand_dictionary(hand)
    # print hand_dict
    pair_values = []
    for key in hand_dict:

        if hand_dict[key] == 2:
            #print key
            pair_values.append(key)

    pair_values = sorted(pair_values)

    pair_values.reverse()
    return pair_values

def which_3_of_a_kind(hand):
    hand_dict = hand_dictionary(hand)
    # print hand_dict
    trip_value = None
    for key in hand_dict:

        if hand_dict[key] == 3:

            trip_value = key

    return trip_value

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


test_hand = ['TC', '5S', '9C', '9S', 'KD']
#
# print which_pair(test_hand)




# print has_straight(test_hand)


# print highest_card(test_hand)

def hand_strength(hand):

    if has_flush(hand) and has_straight(hand):
        return[10, highest_card(hand)]
    elif has_flush(hand):
        return [9, highest_card(hand)]
    elif has_4_of_a_kind(hand):
        return [8]
    elif has_full_house(hand):
        return [7]
    elif has_straight(hand):
        return [6, highest_card(hand)]
    elif has_3_of_a_kind(hand):
        return [5, which_3_of_a_kind(hand)]
    elif has_2_pair(hand):
        return [4, which_2_pair(hand)[0], which_2_pair(hand)[1]]
    elif has_pair(hand):
        return [3, which_pair(hand), get_hand_value_array(hand)[0]]
    else:
        return [2, get_hand_value_array(hand)[0],get_hand_value_array(hand)[1]]



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

