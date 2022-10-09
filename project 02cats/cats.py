"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    filtered_paragraphs = [p for p in paragraphs if select(p)]
    if k >= len(filtered_paragraphs):
        return ''
    else:
        return filtered_paragraphs[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def about_topics(quotes):
        quotes_for_real=split(lower(remove_punctuation(quotes)))
        for i in topic:
            if i in quotes_for_real:
                return True
        return False
    return about_topics
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    num_of_typed,num_of_reference,num_of_correct_words=len(typed_words),len(reference_words),0
    
    if num_of_typed==0:
        return 0.0
    for i in range(num_of_reference+1):
        
        if i==num_of_typed or i==num_of_reference:
            return (num_of_correct_words/num_of_typed)*100
        elif reference_words[i]==typed_words[i]:
            num_of_correct_words+=1
        
            
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    words_length=len(typed)
    return words_length/elapsed*12
    # END PROBLEM 4



def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    
    most_suitable_word=min(valid_words,key = lambda i:diff_function(i,user_word,limit))# 得到差距最小的单词
    pack=diff_function(user_word,most_suitable_word,limit)#得到差距的大小
    if user_word in valid_words:
        return user_word
    elif pack>limit:
        return user_word
    else:
        return most_suitable_word
    
      
    
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    min_length=min(len(start),len(goal))
    def shifty_helper(start,goal,k):    #n:num of recursion  k:num of difference
        if k>limit:
            return 1
        if len(start) == 0:
            return len(goal)
        if len(goal) == 0:
            return len(start)
        else:
            if start[0]==goal[0]:
                
                return shifty_helper(start[1:],goal[1:],k)
            else:
                
                return shifty_helper(start[1:],goal[1:],k+1)+1
    return shifty_helper(start,goal,0)  
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    
    if limit<0:
        return 20031130+1663739463000 #时间戳
    if len(start)==0:
        return len(goal)
    if len(goal)==0:
        return len(start)
    elif start[0]==goal[0]:
        return pawssible_patches(start[1:],goal[1:],limit)
    else:
        add_diff =pawssible_patches(start,goal[1:],limit-1)+1
        remove_diff =pawssible_patches(start[1:],goal,limit-1)+1 
        substitute_diff =pawssible_patches(start[1:],goal[1:],limit-1)+1 
        return min(add_diff,remove_diff,substitute_diff)  
    

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    typed_count, k = 0, 0
    while k < len(typed):
        if k==len(prompt):
            k=len(typed)# 跳出循环
        if typed[k] == prompt[k]:
            typed_count += 1
        else:
            k = len(typed) 
        k += 1

    progress = typed_count / len(prompt)
    message={}
    message['id'], message['progress'] = user_id, progress

    send(message)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    L1=len(words)
    L2=len(times_per_player)
    times=[[times_per_player[i][j]-times_per_player[i][j-1] for j in range(1,L1+1)] for i in range(L2) ]
    result= game(words,times)
    return result
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    result = []
    for _ in player_indices:
        result.append([])
    for w in word_indices:
        find_player_time_for_word_w = lambda player: time(game, player, w)
        fastest_player = min(player_indices, key=find_player_time_for_word_w)
        
        result[fastest_player].append(word_at(game, w))
    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)