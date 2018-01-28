#Mae Aubrey Baes
#github.com/aubreybaes
#DATA STRUCTURES AND ALGORITHM ANALYSIS
#A SIMPLE PALINDROME CHECKER


#enter the palindrome and define it
#I've used part of Peter Norvig's Palindrome

aub = "A man a plan a cameo Zena Bird Mocha Prowel a rave Uganda Wait a lobola Argo Goto Koser Ihab Udall a revocation Ebarta Muscat eyes Rehm a cession Udella Eboat OAS a mirage IPBM a caress Etam FCA a mica Ojai Lebowa Yaeger a barge Rab Alsatian a mod Adv a rps Ileane Valeta Grenada Hetty Fayme REME HCM Tsan Owena Tamar Yompur Isa Nil Lorrin RikSkirnir Rollin a sirup Moyra Matane Won ASTM ChemE Remy a fytte Had an ergate Lavena Elis Pravda Dom an ait a slab a regr a barege a yaw Obelia Joacima a cfm a tessera Camb Piegari Masao Tao Bealle Dunois SECAM Herse Yetac Sumatra Benoit a coverall a dub a hire Sokoto Gogra a lobo Lati a wadna Guevara Lew Orpah Comdr Ibanez OEM a canal Panama"
print aub

#I use replace to remove all spaces, since remove can't be used in string

aub = aub.replace(" ","")
aub = aub.lower()

#convert the string into list
aub_list = list(aub)


#reverse the list
aub_rev = aub_list[::-1]


#conditional statement
if aub_rev == aub_list:					print ("\n\n\n IT'S A PALINDROME BESHY")
else:								print ("\n\n\n SORRY IT'S NOT PALINDROME")

