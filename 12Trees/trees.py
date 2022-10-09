[x*2 for x in range(10)]
odds=[1,3,5,7,9,11]
a=odds[1:-1]

# define tree recursion
def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'我家门口有两棵树，一棵是枣树，另一棵居然不是树'
    return [label]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):  #tree(1)在此变为了empty list，不参加for循环
        if not is_tree(branch):
            return False
    return True
'注意理解tree函数，就是tree(1)不会触发is_tree函数，所以tree（1）是个tree'
def is_leaf(tree):
    return not branches(tree)

#build a fib_tree
def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right=fib_tree(n-1),fib_tree(n-2)
    return tree(label(left)+label(right),[left,right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branches_count=[count_leaves(t) for t in branches(tree)]



def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def fact(n,k=1):
    if n==0:
        return k
    else:
        return fact(n-1,n*k)
print(fact(4))