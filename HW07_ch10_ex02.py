# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(lst):
    upper_lst = []
    for i in lst:
        if isinstance(i,str):
            upper_lst = upper_lst + [i.upper()]
        else:
            upper_lst = upper_lst + [capitalize_nested(i)]
    return upper_lst

def main():
    pass
    #print(capitalize_nested(['a','b',['adasdas',['ad','a'],'asd'],'asdas']))

if __name__ == '__main__':
    main()

    
