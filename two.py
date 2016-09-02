b = 'a = %s\nb = %s\nprint a %% (repr(b), repr(a))'
a = 'b = %s\na = %s\nprint b %% (repr(a), repr(b))'
print b % (repr(a), repr(b))
