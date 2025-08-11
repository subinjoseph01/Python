# union
a = {"john ","alice","bob","diana"}
b={"bob","charlie","diana","eva"}

print(a|b)

# Ans = {'alice', 'charlie', 'diana', 'bob', 'eva', 'john '}



# intersection
a = {"john ","alice","bob","diana"}
b={"bob","charlie","diana","eva"}

print(a&b)
# Ans = {'diana', 'bob'}


# symmetric difference
a = {"john ","alice","bob","diana"}
b={"bob","charlie","diana","eva"}

print(a^b)
# ans = {'charlie', 'alice', 'eva', 'john '}
