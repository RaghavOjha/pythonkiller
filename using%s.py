myname=("Raghav Ojha")
myage=(15)
# not a lie
myheight=(165) # centimetres
myweight=(60) # kg
myeyes=('Black')
myteeth=('White')
myhair = ('Black')
print ("Lets talk about %s.") %(myname)
print ("He is %d inches tall.") %(myheight)
print ("He is %d pounds heavy.") %(myweight)
print ("Actually that is not too heavy.")
print ("He is got %s eyes and %s hair.") %(myeyes, myhair)
print ("His teeth are usually %s depending on the time.") % (myteeth)
# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d.") %(myage, myheight, myweight, myage + myheight + myweight)
