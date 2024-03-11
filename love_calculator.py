m_name=input("Enter name of male partner: ")
f_name=input("Enter name of female partner: ")
combined=m_name.lower()+f_name.lower()
t=combined.count("t")
r=combined.count("r")
u=combined.count("u")
e=combined.count("e")
l=combined.count("l")
o=combined.count("o")
v=combined.count("v")
total1=t+r+u+e
total2=l+o+v+e
love_score=int(str(total1)+str(total2))
if love_score<10 or love_score>90:
    print("hurrey!!",love_score)
elif love_score>=40 and love_score<=80:
    print("your love score is",love_score)
else:
    print("sorry",love_score)