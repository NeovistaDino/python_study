print("%s, %s"("20, 29"))

"""
TypeError: not enough arguments for format string
현재 arguments는 1개("20, 29") 이고
format %s는 2개("%s, %s")이다.
답: arguments를 2개로("20", "29") 늘려주거나
format을 ("%s", "%s")를 1로 줄여준다

해결방법 :
print("%s, %s"("20", "29")) 
"""