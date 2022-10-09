LAB_SOURCE_FILE = __file__



this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    if n<=0:
        return 0
    else:
        return n+skip_add(n-2)
    


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1,'$$n in N$$'
    if n==1:
        return term(1)
    else:
        return term(n)+summation(n-1,term)
    
    


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m==1 or n==1:
        return 1
    else:
        return paths(m-1,n)+paths(m,n-1)



def digits_count(n):
    if n//10==0:
        return 1
    else:
        all_but_last=n//10
        return digits_count(all_but_last)+1
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maximum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    if t==0:
        return 0
    elif digits_count(n)<=t:
        return n
        
    else:
        all_but_last,last=n//10,n%10
        use_last_num=max_subseq(all_but_last,t-1)*10+last
        not_use_last_num=max_subseq(all_but_last,t)
        return max(use_last_num,not_use_last_num)
        

def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    if len(w1)==0:
        return w2
    elif w1[0] in w2[0]:
        w1=w1[1:]
        w2=w2[1:]
        return add_chars(w1,w2)
    else:
        w2n=w2[1:]
        return w2[0]+add_chars(w1,w2n)
a=[0,1,2,3]
print(a[0:])
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
                
                return shifty_helper(start[1:],goal[1:],k+1)
            else:
                
                return shifty_helper(start[1:],goal[1:],k)+1
    return shifty_helper(start,goal,0)  
    # END PROBLEM 6
    
a=[[0,1],[1,2],[2,3]]
experiment=min(a,key=lambda x:x[0])
print(experiment)

    
    
