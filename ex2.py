from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, iam the %s script." %(script, user_name)
print "I'd like to ask you some question."
print "Do you like me %s?" %(user_name)
liking = raw_input(prompt)

print "Where do you live %s?" %(user_name)
living = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """So you said %r about liking me.
Live in %r. Not sure where that is.
And use a %r pc. Nice.
""" % (liking, living, computer)