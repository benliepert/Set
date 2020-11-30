
def isSet(card1,card2,card3):

    for i in range(4):
        if card1[i] == card2[i] and card1[i] == card3[i] and card2[i] == card3[i]:
            # attribute i matches
            pass
        elif card1[i] != card2[i] and card1[i] != card3[i] and card2[i] != card3[i]:
            # attribute i doesn't match
            pass
        else:
            return False

    return True

def findSets(cards):
    sets = []

    #there will never be duplicates

    for card1 in cards:

        for card2 in cards:

            if card2 != card1:

                for card3 in cards:

                    if card3 != card2 and card3 != card1:
                        
                        # now we do some stuff, since any set is possible given just two cards, its the third card that ruins the bunch
                        if isSet(card1,card2,card3):
                            if (card3,card1,card2) in sets or (card1, card3, card2) in sets or (card2, card1, card3) in sets or (card2, card3, card1) in sets or (card3, card2, card1) in sets:
                                pass
                            else:
                                sets.append((card1,card2,card3)) # could sort and then append. would that help shorten the if statement above?
    return sets

def main():
    cards = []

    numCards = int(input("How many cards are you playing with?: "))

    if numCards < 3:
        print("Well thats no fun...")
        return

    print("Color attribute should be entered as r (red), g (green), or p (purple)")
    print("Shape attribute should be entered as o (oval), s (squiggle), or d (diamond)")
    print("Shading attribute should be entered as n (none), s (shaded), or f (filled)")
    print("Number of shapes attribute should be entered as a single number (1, 2 or 3)")
    for i in range(numCards):
        print("Please enter the attributes for card number {}.".format(i+1))
        color = input("Color (r, g, or p): ").strip()
        shape = input("Shape (o, s or d): ").strip()
        shading = input("Shading (n, s, or f): ").strip()
        numShapes = int(input("Number of shapes: ").strip())
        cards.append((color,shape,shading,numShapes))

    print("You entered the following cards:")
    for card in cards:
        print(card)

    sets = findSets(cards)

    if len(sets) == 0 :
        print("No sets exist!")
    else:
        resp = "y"#input("At least one set exists! Would you like to know them? (y or n): ")
        if resp == 'y':
            for s in sets:
                print(s)
        else:
            print("Good luck finding it!")

main()
