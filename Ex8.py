formatter = "{} {} {} {}"# the  {} acts as placement spot because when I removed
# a {} the 4,four,{}{}{}{},and "or a song about of fear wont appear

print(formatter.format(1, 2, 3, 4))#formatter.format makes so that if a
print(formatter.format("one", "two", "three", "four"))#{} is missing then the last spot wont appear
print(formatter.format(True, False, False, True))#ex only three{} the four wont appear
print(formatter.format(formatter, formatter, formatter, formatter))#use of a variable
#to print 16 {} without typing it all out
print(formatter.format(
    "Try your",
    "Own text here ",
    "Maybe a poem",
    "Or a song about fear"
 ))#Text that maybe missing a line if {} are missing
