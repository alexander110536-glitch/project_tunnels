"""
Filename: text-based_adventure_game.py
Author: <Alexander Cruz>
Created: <10/13/2025>
Instructor: Holtslander
Description: Text-Based_adventure_game
    <DESCRIPTION OF THE PROGRAM>
Dependencies: parser
"""

# Import statements
from parser import Parser

# This is a dictionary
# It is a place to store variables you want to use in your story Instead of having to create and manage many different
# variables, we can just store and quickly access them here.
# Inserting a new entry: player_vars["key"] = "value"
# If you want to store a user generated value: player_vars["player"] = input("Please type your name")
# "key" is your variable name and "value" is what you are storing. (It can also be an integer. Just remove the quotes.)
#
# Accessing an entry: player_vars["key"]
# e.g.
# print(player_vars["key"])
#
# You can also overwrite an entry by just assigning a new value e.g.: player_vars["key"] = "value2"
player_vars = {
    "player" : "Henry"
}

# This is the entry point for the program. It the program should start and stop here.
# For now, all your code should be in the main function
def main():
    """
    The entry point and driver of the narrative game program.
    :return: None
    """

    # This creates a new parser object. You can use it to print your text files
    # parser.dprint("example.txt", player_vars, pause=0.1)
    # The dict and pause arguments can be omitted if you do not want a delay and do not want to format the output.
    parser = Parser()

    # Your code goes under this line.

    p = 0
    parser.dprint("Start.txt", player_vars, pause=p)
    c1 = input()
    if c1 =="left":
        parser.dprint("Left.txt", player_vars, pause=p)
        c2 = input()
        if c2 =="search":
            parser.dprint("sherch.txt", player_vars, pause=p)

        else:
            c2 =="stay"
            parser.dprint("stay.txt", player_vars, pause=p)
    #search
    
            c4 = input()
            if c4 =="right tunnel":
                parser.dprint("right_tunnel.text", player_vars, pause=p)

            else:
                c4 = "left tunnel"
                parser.dprint("left_tunnel.text", player_vars, pause=p)
    #stay
    
            c5 = input()
            if c5 =="stay again":
                parser.dprint("stay_again.txt", player_vars, pause=p)

            else:
                c5 = "look for exit"
                parser.dprint("start_looking_for_exit.txt", player_vars, pause=p)
    #right tunnel
    
            c6 = input()
            if c6 =="stay hidden":
                parser.dprint("stay_hidden.txt", player_vars, pause=p)

            else:
                c6 = "fight"
                parser.dprint("Fight.txt", player_vars, pause=p)
    
    #stay again
    
            c8 = input()
            if c8 =="don't go":
                parser.dprint("Stay_four.txt", player_vars, pause=p)

            else:
                c8 = "no"
                parser.dprint("No.txt", player_vars, pause=p)

    #stay hidden
    
            c7 = input()
            if c7 =="leave him":
                parser.dprint("leave_him.txt", player_vars, pause=p)

            else:
                c7 = "stay with him"
                parser.dprint("stay_with_him.txt", player_vars, pause=p)
    #Look for exit
    
            c9 = input()
            if c9 =="you leave them":
                parser.dprint("you_leave_them.txt", player_vars, pause=p)

            else:
                c9 = "stay three"
                parser.dprint("Stay_3.txt", player_vars, pause=p)
    #stay 3
    
            c10 = input()
            if c10 =="say something":
                parser.dprint("Say_something.txt", player_vars, pause=p)

            else:
                c10 = "spy on him"
                parser.dprint("Spy_on_him.txt", player_vars, pause=p)
    #no
    
            c10 = input()
            if c10 =="say something":
                parser.dprint("Say_something.txt", player_vars, pause=p)

            else:
                c10 = "spy on him"
                parser.dprint("Spy_on_him.txt", player_vars, pause=p)
    #say something
    
            c11 = input()
            if c11 =="don't believe":
                parser.dprint("don't_believe.txt", player_vars, pause=p)

            else:
                c11 = "believe"
                parser.dprint("Believe.txt", player_vars, pause=p)



#we will change pass later
#part 2: create right file change pass to righttxt
    else:
        parser.dprint("Right.txt", player_vars, pause=p)
        q18 = input()
        if q18 =="follow shadow":
            parser.dprint("Follow_shadow.txt", player_vars, pause=p)

        else:
            q18 =="ignore"
            parser.dprint("Ignore.txt", player_vars, pause=p)
    #follow shadow
    
            q4 = input()
            if q4 =="follow isamu":
                parser.dprint("follow_Isamu.txt", player_vars, pause=p)

            else:
                q4 = "exit"
                parser.dprint("Exit.txt", player_vars, pause=p)
    #ignore
    
            q5 = input()
            if q5 =="treat his wound":
                parser.dprint("Treat_wound.txt", player_vars, pause=p)

            else:
                q5 = "keep going"
                parser.dprint("Keep_going.txt", player_vars, pause=p)
    #Follow isamu
    
            q6 = input()
            if q6 =="run":
                parser.dprint("Run.txt", player_vars, pause=p)

            else:
                q6 = "what happens"
                parser.dprint("What_happens.txt", player_vars, pause=p)
    
    #treat his wound
    
            q8 = input()
            if q8 =="give katana":
                parser.dprint("Give_katana.txt", player_vars, pause=p)

            else:
                q8 = "run two"
                parser.dprint("Run_two.txt", player_vars, pause=p)
    
    #stay hidden
    
            q7 = input()
            if q7 =="leave him":
                parser.dprint("leave_him.txt", player_vars, pause=p)

            else:
                q7 = "stay with him"
                parser.dprint("stay_with_him.txt", player_vars, pause=p)
    #keep going
    
            q9 = input()
            if q9 =="collapse":
                parser.dprint("collapse.txt", player_vars, pause=p)

            else:
                q9 = "run straight"
                parser.dprint("Run_straight.txt", player_vars, pause=p)
    
    #give katana
    
            q10 = input()
            if q10 =="accept duel":
                parser.dprint("Accept_duel.txt", player_vars, pause=p)

            else:
                q10 = "you go looking"
                parser.dprint("You_go_looking.txt", player_vars, pause=p)
    #accept duel
    
            q11 = input()
            if q11 =="throw rocks":
                parser.dprint("Don't_help.txt", player_vars, pause=p)

            else:
                q11 = "don't help"
                parser.dprint("Help.txt", player_vars, pause=p)


    # Clean up code. Do not write any code past this line.
    parser.destroy()
    parser = None

# This tells the program to start with the main function.
if __name__ == "__main__":
    main()
