a = 'b = %s\nc = %s\na = %s\nprint b %% (repr(c), repr(a), repr(b))'
b = 'c = %s\na = %s\nb = %s\nprint c %% (repr(a), repr(b), repr(c))'
c = 'a = %s\nb = %s\nc = %s\nprint a %% (repr(b), repr(c), repr(a))'
print a % (repr(b), repr(c), repr(a))
