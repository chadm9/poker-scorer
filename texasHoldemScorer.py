

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

    if player_hand == [2,3,4,5,14]:
        return True


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


def has_4_of_a_kind(hand):
    hand_dict = hand_dictionary(hand)

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
    single_card_value = None
    pair_values = []
    for key in hand_dict:

        if hand_dict[key] == 2:
            #print key
            pair_values.append(key)
        elif hand_dict[key] == 1:
            single_card_value = key

    pair_values = sorted(pair_values)

    pair_values.reverse()
    pair_values.append(single_card_value)
    return pair_values

def which_3_of_a_kind(hand):
    hand_dict = hand_dictionary(hand)
    # print hand_dict
    trip_value = None
    for key in hand_dict:

        if hand_dict[key] == 3:

            trip_value = key

    return trip_value


def which_4_of_a_kind(hand):
    hand_dict = hand_dictionary(hand)
    # print hand_dict
    trip_value = None
    for key in hand_dict:

        if hand_dict[key] == 4:

            trip_value = key

    return trip_value


def highest_card(hand):
    highest_card_value = 0
    for i in range(len(hand)):
        current_card_value = convert_to_int(hand[i][0])

        if current_card_value > highest_card_value:
            highest_card_value = current_card_value

    return highest_card_value


def hand_strength(hand):

    if has_flush(hand) and has_straight(hand):
        return[10, highest_card(hand)]
    elif has_4_of_a_kind(hand):
        return [9, which_4_of_a_kind(hand)]
    elif has_full_house(hand):
        return [8, which_3_of_a_kind(hand)]
    elif has_flush(hand):
        return [7, get_hand_value_array(hand)[0], get_hand_value_array(hand)[1], get_hand_value_array(hand)[2],
                get_hand_value_array(hand)[3], get_hand_value_array(hand)[4]]
    elif has_straight(hand):
        return [6, highest_card(hand)]
    elif has_3_of_a_kind(hand):
        return [5, which_3_of_a_kind(hand)]
    elif has_2_pair(hand):
        return [4, which_2_pair(hand)[0], which_2_pair(hand)[1], which_2_pair(hand)[2]]
    elif has_pair(hand):
        return [3, which_pair(hand), get_hand_value_array(hand)[0], get_hand_value_array(hand)[1], get_hand_value_array(hand)[2],
                get_hand_value_array(hand)[3], get_hand_value_array(hand)[4]]
    else:
        return [2, get_hand_value_array(hand)[0], get_hand_value_array(hand)[1], get_hand_value_array(hand)[2],
                get_hand_value_array(hand)[3], get_hand_value_array(hand)[4]]

def unique_5_card_combinations(lyst, combination=[], combinations=[]):
    #print combination
    if len(combination) == 5:
        if sorted(combination) not in combinations:
            combinations.append(sorted(combination))
        #print combinations
    for i in range(len(lyst)):
        if lyst[i] not in combination:
            combination.append(lyst[i])

            unique_5_card_combinations(lyst, combination, combinations)
            combination.pop()


    return combinations






def best_5_card_combination(seven_card_hand):

    possible_hands = unique_5_card_combinations(seven_card_hand, [], [])
    best_hand = possible_hands[0]


    for this_hand in possible_hands:
        best_hand_strength = hand_strength(best_hand)
        this_hand_strength = hand_strength(this_hand)
        counter = 0

        while (best_hand_strength[counter] == this_hand_strength[counter] and counter < (len(best_hand_strength) - 1)):
            counter += 1

        if best_hand_strength[counter] < this_hand_strength[counter]:
            best_hand = this_hand

    return best_hand




def get_winner(hand1, hand2):
    # print hand1
    # print hand2
    player_1_hand = best_5_card_combination(hand1)
    player_2_hand = best_5_card_combination(hand2)

    # print player_1_hand
    # print player_2_hand

    player_1_hand_strength = hand_strength(player_1_hand)
    player_2_hand_strength = hand_strength(player_2_hand)
    counter = 0

    while (player_1_hand_strength[counter] == player_2_hand_strength[counter] and counter < (len(player_1_hand_strength) - 1)):
        counter += 1

    if player_1_hand_strength[counter] > player_2_hand_strength[counter]:
        return {'winner': 'player 1', 'loser': 'player 2', 'player1sHand': player_1_hand,
                'player2sHand': player_2_hand}
    elif player_2_hand_strength[counter] > player_1_hand_strength[counter]:
        return {'winner': 'player 2', 'loser': 'player 1', 'player1sHand': player_1_hand,
                'player2sHand': player_2_hand}
    else:
        return {'winner': 'tie', 'loser': 'tie', 'player1sHand': player_1_hand,
                'player2sHand': player_2_hand}

# test_hand1 = ['5H', '6H', 'KH', '2H', '3H', 'QD', 'AH']
# test_hand2 = ['2H', '3H', '4H', '5D', '3D', 'QS', 'AS']
# test_hand3 = ['5D', '5H', '5S', '2D', '2H', 'QD', 'AS']
#
# print get_winner(test_hand1, test_hand2)




