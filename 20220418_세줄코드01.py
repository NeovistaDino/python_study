dino_age = "20"
#dino_age에 string"20"저장

young_age = "29"
#young_age에 string"29"저장

print("%s", "%s" %(dino_age, young_age))
#출력 format %s는 2개 string은 2개(dino_age, young_age)



"""
string 변수 : 2개(dino_age, young_age)

각각 "20", "29"을 대입(저장)을 하고,

함수 print() 이용해서 출력하시오.

결과:
20, 29
"""

"""
TypeError: not all arguments converted during string formatting
           모든 arguments가 변환되지 않았다. string이 formatting하는 중에
"""