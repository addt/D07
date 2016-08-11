# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_list(lst):
    cum_list = []
    for i in range(1, len(lst)+1):
        cum_list = cum_list + [sum(lst[:i])]
    return cum_list


#tt = [3,4,1,6,2,3,5]
#print(cumulative_list(tt))


def main():
    pass
    
if __name__ == '__main__':
    main()
        
