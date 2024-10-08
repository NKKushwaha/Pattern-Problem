#1. WAPT print the squre pattern problem
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        print('*', end=' ')
    print()

'''

'''
n=int(input())
for row in range (1,n+1):
        print('* '*n)
'''


#2. WAPT print the digonal problem
'''
*         
  *       
    *     
      *   
        *
'''
'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        if row==col:
            print('*', end=' ')
        else:
            print(' ', end =' ')
    print()

'''

#3. WAPT print the reverse digonal problem

'''
        * 
      *   
    *     
  *       
*         
'''
'''

n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        if (row+col)==(n+1):
            print('*', end=' ')
        else:
            print(' ', end =' ')
    print()
'''



#4. WAPT print the left primide
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

'''
n=int(input())
for row in range (1,n+1):
    print('* ' *row)
'''

'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,row+1):
        print('*', end=' ')
    print()
'''

'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        if row>=col:
            print('*',end=' ')
    print()
'''

#5. WAPT print the right primide
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''
'''

n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        if row+col>=n+1:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()

'''
#6. WAPT print the upside right primide
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''
'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()
'''

#7. WAPT print the upside left primide
'''
* * * * * 
* * * * 
* * * 
* * 
*
'''

'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,n+1):
        if row<=col:
            print('*',end=' ')
    print()

'''


#8. Genric approch for left digonal pattern
'''
* 
  * 
    * 
      * 
        * 
'''
'''
n=int(input())
starts=1
spaces=0
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    spaces+=1
'''
#9. Genric approch for right digonal pattern
'''
        * 
      * 
    * 
  * 
*
'''
'''
n=int(input())
starts=1
spaces=n-1
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    spaces-=1
'''



#10. WAPT print the right primide using genric approch
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''

'''
n=int(input())
starts=1
spaces=n-1
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    spaces-=1
    starts+=1
'''


#11. WAPT print the left primide using genric approch


'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

'''
n=int(input())
starts=1
spaces=0
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    starts+=1
'''


#12. WAPT print the upside left primide using grnric approch
'''
* * * * * 
* * * * 
* * * 
* * 
*
'''

'''
n=int(input())
starts=n
spaces=0
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    starts-=1
'''


#13. WAPT print the upside right primide using genric approch
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

'''
n=int(input())
starts=n
spaces=0
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    starts-=1
    spaces+=1
'''

#14. WAPT print the primide
'''
    *
  * * *
* * * * *
'''
'''
n=int(input())
for row in range (1,n+1):
        print(' '*(n-row),end=' ')
        print('*'*(2*row-1))
'''

# genric approch
'''
n=int(input())
starts=1
spaces=n-1
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print('*' ,end=' ')
    print()
    starts+=2
    spaces-=1
'''


#15. WAPT print the opposit primide using gnric approch

'''
* * * * * 
  * * * 
    *
'''

'''

n=int(input())
starts=(2*n)-1
spaces=0
for row in range (1,n+1):
    for sp in range (1,spaces+1):
        print(' ', end=' ')
    for st in range (1, starts+1):
        print('*', end=' ')
    print()
    spaces+=1
    starts-=2
'''


#16. WAPT print right dimand

'''
* 
* * * 
* * * * * 
* * * 
*
'''
'''

n=int(input())
stars=1
for row in range (1,n+1):
    for st in range (1,stars+1):
        print('*', end=' ')
    print()
    if row<=n//2:
        stars+=2
    else:
        stars-=2
'''

#17. WAPT print the Dimand

'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

'''

'''
n=int(input())
stars=1
space=(n//2)
for row in range (1,n+1):
    for sp in range (1,space+1):
        print(' ' ,end=' ')
    for st in range (1, stars+1):
        print('*' , end=' ')
    print()
    if row<=n//2:
        stars+=2
        space-=1
    else:
        stars-=2
        space+=1
'''      


#18. WAPT print the square with the row wise incremantation

'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5
'''

'''
n = int(input())
dummy=1
for row in range (1,n+1):
    for col in range(1,n+1):
        print(dummy, end=' ')
    print()
    dummy+=1
'''

#19. WAPT print the square with the column incrementation
'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in range (1, n+1):
        print(dummy, end=' ')
        dummy+=1
    print()
'''  


#20. WAPT print the digonal row increment
'''
1         
  2       
    3     
      4   
        5 
'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    for col in range (1,n+1):
        if row==col:
            print(dummy,end=' ')
        else:
            print(' ', end=' ')
    print()
    dummy+=1
'''

#21. WAPT print the opposit digonal row increment
'''
        1 
      2   
    3     
  4       
5
'''
'''

n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range (1,n+1):
        if row+col== n+1:
            print(dummy, end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
'''


#22. WAPT print the given pattern

'''
5 * 4 * 3 * 2 * 1

4 * 3 * 2 * 1

3 * 2 * 1

2 * 1

1
'''

'''
n=int(input())
rdummy=n
for row in range (n,0,-1):
    dummy=rdummy
    for col in range (1,row+1):
        if col==row:
            print(dummy)
        else:
            print(dummy, end=' * ')
            dummy-=1
    rdummy-=1 
    print()
'''


#23. 


'''
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
'''

'''
n=int(input())
c=1
for row in range (1,n+1):
    for col in range (1,n+1):
        if row>=col:
            print(c, end=' ')
        else:
            print(col, end=' ')
    print()
    c+=1
'''



#24. 

'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in range (1,n+1):
        print(dummy, end=' ')
        dummy+=1
    print()
'''



#25.


'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    for col in range (1,n+1):
        print(dummy, end=' ')

    print()
    dummy+=1
'''



#26.

'''
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25
'''
'''

n=int(input())
dummy=1
for row in range (1,n+1):
    dummy1=dummy
    for col in range (1,n+1):
        print(dummy1, end=' ')
        dummy1+=1
    dummy=dummy1
    print()
'''


#27.


'''
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
6 7 8 9 10
'''
'''
n=int(input())
dummy=1
for row in range (0,n+1):
    dummy1=dummy
    for col in range (1,n+1):
        print(dummy1, end=' ')
        dummy1+=1
    print()
    dummy+=1
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in range (1,n+1):
        print(dummy, end =' ')
        dummy+=1
    print()
'''

#28.

'''
1 6 11 16 21 
2 7 12 17 22 
3 8 13 18 23 
4 9 14 19 24 
5 10 15 20 25
'''
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    dummy1=dummy
    for col in range (1,n+1):
        print(dummy1, end= ' ')
        dummy1+=5
    print()
    dummy+=1
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in range (1,n+1):
        print(dummy, end =' ')
        dummy+=5
    print()
'''



#29.
'''
1 2 3 4 5 
2 4 6 8 10 
3 4 5 6 7 
4 6 8 10 12 
5 6 7 8 9
'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    dummy1=dummy
    for col in range(1,n+1):
        print(dummy1, end=' ')
        if dummy%2==0:
            dummy1+=2
        else:
            dummy1+=1
    print()
    dummy+=1
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy, end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
'''



#30.

'''
1         
1 2       
1 2 3     
1 2 3 4   
1 2 3 4 5
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in range(1,n+1):
        if row>=col:
            print(dummy , end=' ')
            dummy+=1
        else:
            print(' ', end= ' ')
    print()

'''


#31.

'''
1         
2 2       
3 3 3     
4 4 4 4   
5 5 5 5 5
'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    for col in range (1,n+1):
        if row>=col:
            print(dummy, end= ' ')
        else:
            print(' ' , end= ' ')
    print()
    dummy+=1
'''




#32.
'''
1 2 3 4 5 
1 2 3 4   
1 2 3     
1 2       
1         

'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in  range (1,n+1):
        if row+col<=n+1:
            print(dummy, end=' ')
            dummy+=1
        else:
            print(' ', end=' ')
    print()
'''



#33.
'''
        1 
      2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1 
'''
'''

n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in  range (1,n+1):
        if row+col>=n+1:
            print(dummy, end=' ')
            dummy-=1
        else:
            print(' ', end=' ')
    print()
'''




#34.

'''
5 4 3 2 1 
  4 3 2 1 
    3 2 1 
      2 1 
        1
'''
'''

n=int(input())
dummy=n
spaces=0
for row in range (1,n+1):
    dummy1=n
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,dummy+1):
        print(dummy1 ,end=' ')
        dummy1-=1
    print()
    n-=1
    dummy-=1
    spaces+=1
'''




#35.
'''
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
'''
'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,row):
        print (col, end=' ')
    for col in range (row,0,-1):
        print (col, end= ' ')
    print()
'''




#36.
'''
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 3 4 5   
5 4 3 3 4 5     
5 4 4 5       
5 5
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=n
    for col in  range (1,n+1):
        if row+col<=n+1:
            print(dummy, end=' ')
            if dummy!=row:
                dummy-=1
    for col in  range (1,n+1):
        if row+col<=n+1:
            print(dummy, end=' ')
            dummy+=1
        else:
            print(' ', end=' ')
    print()
 '''       




#37.
'''
        1 
      2 1 2 
    3 2 1 2 3 
  4 3 2 1 2 3 4 
5 4 3 2 1 2 3 4 5 
'''
'''
n=int(input())
starts=1
spaces=n-1
for row in range (1,n+1):
    dummy=row
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print(dummy ,end=' ')
        if st<=starts//2:
            dummy-=1
        else:
            dummy+=1  
    print()
    starts+=2
    spaces-=1
'''


#38.    
'''
5 5 5 5 5 
5 4 4 4 4 
5 4 3 3 3 
5 4 3 2 2 
5 4 3 2 1 
'''

'''
n=int(input())
c=n
for row in range (1,n+1):
    dummy=c
    for col in range (1,n+1):
        print(dummy, end=' ')
        if row>col:
            dummy-=1  
    print()
'''


#39.
'''
0             
0 1           
0 2 4         
0 3 6 9       
0 4 8 12 16     
0 5 10 15 20 25   
0 6 12 18 24 30 36

'''
'''
n=int(input())
for row in range (0,n+1):
    for col in range (0,n+1):
        if row>=col:
            print(row*col, end=' ')
        else:
            print(' ' , end= ' ')
    print()
'''



#40.
'''
1         
3 2       
6 5 4     
10 9 8 7   
'''
'''
n=int(input())
c=1
for row in range(1,n+1):
    dummy=c
    for col in range(1, n+1):
        if row>=col:
            print(dummy, end=' ')
            dummy-=1
        else:
            print(' ',end= ' ')
    print()
    c+=1+row
'''


#41.
''''
        1 
      3 2 
    5 4 3 
  7 6 5 4 
9 8 7 6 5

'''
'''
n=int(input())
c=1
for row in range (1,n+1):
    dummy=c
    for col in  range (1,n+1):
        if row+col>=n+1:
            print(dummy, end=' ')
            dummy-=1
        else:
            print(' ', end=' ')
    print()
    c+=2
'''




#42.
'''
@             
@ A           
@ B D         
@ C F I       
@ D H L P     
@ E J O T Y   
@ F L R X ^ d
'''
'''
n=int(input())
for row in range (0,n+1):
    for col in range (0,n+1):
        if row>=col:
            print(chr(64+row*col), end=' ')
        else:
            print(' ' , end= ' ')
    print()
'''

#43.
'''
E E E E E 
E D D D D 
E D C C C 
E D C B B 
E D C B A 

'''
'''
n=int(input())
c=n
for row in range (1,n+1):
    dummy=c
    for col in range (1,n+1):
        print(chr(64+dummy), end=' ')
        if row>col:
            dummy-=1  
    print()
'''


#44.
'''
        A 
      B A B 
    C B A B C 
  D C B A B C D 
E D C B A B C D E 
'''
'''
n=int(input())
starts=1
spaces=n-1
for row in range (1,n+1):
    dummy=row
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,starts+1):
        print(chr(64+dummy) ,end=' ')
        if st<=starts//2:
            dummy-=1
        else:
            dummy+=1
            
    print()
    starts+=2
    spaces-=1
'''


#45.
'''
p           
p y         
p y t       
p y t h     
p y t h o   
p y t h o n
'''
'''
s=input()
n=len(s)
for row in range (1,n+1):
    c=1
    for col in s:
        if row>=c:
            print(col, end=' ')
            c+=1
        else:
            print(' ', end=' ')
            
    print()
'''




#46. WAPT print the square with the row wise incremantation

'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
'''

'''
n = int(input())
dummy=1
for row in range (1,n+1):
    for col in range(1,n+1):
        print(chr(64+dummy), end=' ')
    print()
    dummy+=1
'''

#47. WAPT print the square with the column incrementation
'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 
'''

'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in range (1, n+1):
        print(chr(64+dummy), end=' ')
        dummy+=1
    print()
''' 


#48. WAPT print the digonal row increment
'''
A         
  B       
    C     
      D   
        E 
'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    for col in range (1,n+1):
        if row==col:
            print(chr(64+dummy),end=' ')
        else:
            print(' ', end=' ')
    print()
    dummy+=1
'''

#49. WAPT print the opposit digonal row increment
'''
        A 
      B   
    C     
  D       
E  
'''
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range (1,n+1):
        if row+col== n+1:
            print(chr(64+dummy), end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
'''



#50. WAPT print the given pattern

'''
E * D * C * B * A

D * C * B * A

C * B * A

B * A

A
'''

'''
n=int(input())
rdummy=n
for row in range (n,0,-1):
    dummy=rdummy
    for col in range (1,row+1):
        if col==row:
            print(chr(64+dummy))
        else:
            print(chr(64+dummy), end=' * ')
            dummy-=1
    rdummy-=1 
    print()
'''



#51.

'''
A B C D E 
B B C D E 
C C C D E 
D D D D E 
E E E E E 
'''

'''
n=int(input())
c=1
for row in range (1,n+1):
    for col in range (1,n+1):
        if row>=col:
            print(chr(64+c), end=' ')
        else:
            print(chr(64+col), end=' ')
    print()
    c+=1

'''



#52.
'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in range (1,n+1):
        print(chr(64+dummy), end=' ')
        dummy+=1
    print()
'''




#53.
'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
'''

'''
n=int(input())
dummy=1
for row in range (1,n+1):
    for col in range (1,n+1):
        print(chr(64+dummy), end=' ')

    print()
    dummy+=1
'''




#54.
'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y
'''

'''
n=int(input())
dummy=1
for row in range (1,n+1):
    dummy1=dummy
    for col in range (1,n+1):
        print(chr(64+dummy1), end=' ')
        dummy1+=1
    dummy=dummy1
    print()
'''




#55.

'''
A B C D E 
B C D E F 
C D E F G 
D E F G H 
E F G H I 
F G H I J 
'''

'''
n=int(input())
dummy=1
for row in range (0,n+1):
    dummy1=dummy
    for col in range (1,n+1):
        print(chr(64+dummy1), end=' ')
        dummy1+=1
    print()
    dummy+=1
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in range (1,n+1):
        print(chr(64+dummy), end =' ')
        dummy+=1
    print()
'''


#56.
'''
A F K P U 
B G L Q V 
C H M R W 
D I N S X 
E J O T Y 

'''
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    dummy1=dummy
    for col in range (1,n+1):
        print(chr(64+dummy1), end= ' ')
        dummy1+=5
    print()
    dummy+=1
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in range (1,n+1):
        print(chr(64+dummy1), end =' ')
        dummy+=5
    print()
'''


#57.

'''
A B C D E 
B D F H J 
C D E F G 
D F H J L 
E F G H I 

'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    dummy1=dummy
    for col in range(1,n+1):
        print(chr(64+dummy1), end=' ')
        if dummy%2==0:
            dummy1+=2
        else:
            dummy1+=1
    print()
    dummy+=1
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy1), end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
'''




#58.
'''
A         
A B       
A B C     
A B C D   
A B C D E 
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in range(1,n+1):
        if row>=col:
            print(chr(64+dummy) , end=' ')
            dummy+=1
        else:
            print(' ', end= ' ')
    print()
'''




#59.
'''
A         
B B       
C C C     
D D D D   
E E E E E 
'''
'''
n=int(input())
dummy=1
for row in range (1,n+1):
    for col in range (1,n+1):
        if row>=col:
            print(chr(64+dummy), end= ' ')
        else:
            print(' ' , end= ' ')
    print()
    dummy+=1
'''




#60.
'''
A B C D E 
A B C D   
A B C     
A B       
A         
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=1
    for col in  range (1,n+1):
        if row+col<=n+1:
            print(chr(64+dummy), end=' ')
            dummy+=1
        else:
            print(' ', end=' ')
    print()
'''



#61.
'''
        A 
      B A 
    C B A 
  D C B A 
E D C B A 
'''

'''
n=int(input())
for row in range (1,n+1):
    dummy=row
    for col in  range (1,n+1):
        if row+col>=n+1:
            print(chr(64+dummy), end=' ')
            dummy-=1
        else:
            print(' ', end=' ')
    print()
'''




#62.

'''
E D C B A 
  D C B A 
    C B A 
      B A 
        A 
'''
'''
n=int(input())
dummy=n
spaces=0
for row in range (1,n+1):
    dummy1=n
    for sp in range (1,spaces+1):
        print(' ' ,end=' ')
    for st in range (1,dummy+1):
        print(chr(64+dummy1) ,end=' ')
        dummy1-=1
    print()
    n-=1
    dummy-=1
    spaces+=1
'''





#63.
'''
A 
A B A 
A B C B A 
A B C D C B A 
A B C D E D C B A 
'''
'''
n=int(input())
for row in range (1,n+1):
    for col in range (1,row):
        print (chr(64+col), end=' ')
    for col in range (row,0,-1):
        print (chr(64+col), end= ' ')
    print()
'''




#64.
'''
E D C B A A B C D E 
E D C B B C D E   
E D C C D E     
E D D E       
E E        
'''
'''
n=int(input())
for row in range (1,n+1):
    dummy=n
    for col in  range (1,n+1):
        if row+col<=n+1:
            print(chr(64+dummy), end=' ')
            if dummy!=row:
                dummy-=1
    for col in  range (1,n+1):
        if row+col<=n+1:
            print(chr(64+dummy), end=' ')
            dummy+=1
        else:
            print(' ', end=' ')
    print()
'''   






#65.
    
'''
E E E E E 
E D D D D 
E D C C C 
E D C B B 
E D C B A  
'''

'''
n=int(input())
c=n
for row in range (1,n+1):
    dummy=c
    for col in range (1,n+1):
        print(chr(64+dummy), end=' ')
        if row>col:
            dummy-=1  
    print()
'''









#66.

'''
A         
C B       
F E D     
J I H G   
O N M L K 
'''
'''
n=int(input())
c=1
for row in range(1,n+1):
    dummy=c
    for col in range(1, n+1):
        if row>=col:
            print(chr(64+dummy), end=' ')
            dummy-=1
        else:
            print(' ',end= ' ')
    print()
    c+=1+row
'''



#67.
'''
        A 
      C B 
    E D C 
  G F E D 
I H G F E 
'''
'''
n=int(input())
c=1
for row in range (1,n+1):
    dummy=c
    for col in  range (1,n+1):
        if row+col>=n+1:
            print(chr(64+dummy), end=' ')
            dummy-=1
        else:
            print(' ', end=' ')
    print()
    c+=2
'''

#68.
'''
* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * * 
'''
'''
n=int(input())
for row in range (1,n+1):
    for col in range (1, n+1):
        if row==1 or row==n or col==1 or col==n or row==col or col+row==n+1:
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print()

'''


#69.
'''
* * * * * 
* *   * * 
*   #   * 
* *   * * 
* * * * * 
'''


'''
n=int(input())
for row in range (1,n+1):
    for col in range (1, n+1):
        if row==n//2+1 and col==n//2+1:
            print('#', end=' ')
        elif row==1 or row==n or col==1 or col==n or row==col or row+col==n+1:
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print()
'''

    
#70.

'''
1         
  2       
    3     
  4       
5
'''

'''
n=int(input())
space=0
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range (1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(dummy, end=' ')
        if row<=n//2:
            dummy+=1
            space+=1
        elif row==n//2+1:
            dummy+=n//2
            space-=1
        else:
            dummy-=1
            space-=1
    print()
    
'''

#71.
'''
1 
  3 
    5 
      7 
    6 
  4 
2 
'''
'''
n=int(input())
space=0
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range (1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(dummy, end=' ')
        if row<=n//2:
            dummy+=2
            space+=1
        elif row==n//2+1:
            dummy-=1
            space-=1
        else:
            dummy-=2
            space-=1
    print()
'''

#72
'''
1 
  2 
    3 
      4 
    7 
  6 
5
'''
'''
n=int(input())
space=0
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range (1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(dummy, end=' ')
        if row<=n//2:
            dummy+=1
            space+=1
        elif row==n//2+1:
            dummy=n
            space-=1
        else:
            dummy-=1
            space-=1
    print()
'''




#73

'''
2 
  3 
    5 
      7 
    11 
  13 
17 
'''
'''
n=int(input())
c=0
s=2
l=[]
while True:
    for i in range (2,s//2+1):
        if s%i==0:
            break
    else:
        c+=1
        l.append(s)
        if c==n:
            break     
    s+=1
space=0
stars=1
ip=0        
for row in range (1,n+1):
    for sp in range (1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(l[ip], end=' ')
        if row<=n//2:
            ip+=1
            space+=1
        elif row==n//2+1:
            ip+=1
            space-=1
        else:
            ip+=1
            space-=1
    print()
'''


#74

'''
2 
  3 
    5 
      8 
    13 
  21 
34 
'''

'''
n=int(input())
SUM=0
n1=1
n2=1
l=[]
for i in range (1,n+1):
    SUM=n1+n2
    n1,n2=n2,SUM
    l.append(SUM)
space=0
stars=1
ip=0        
for row in range (1,n+1):
    for sp in range (1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(l[ip], end=' ')
        if row<=n//2:
            ip+=1
            space+=1
        elif row==n//2+1:
            ip+=1
            space-=1
        else:
            ip+=1
            space-=1
    print()
'''


#75

'''
* * * * * * 
* *     * * 
*   # #   * 
*   # #   * 
* *     * * 
* * * * * * 
'''

'''
n=int(input())
for row in range (1,n+1):
    for col in range (1, n+1):
        if row==n//2+1 and col==n//2+1 or row==n//2 and col==n//2 or row==n//2 and col==n//2+1 or row==n//2+1 and col==n//2:
            print('#', end=' ')
        elif row==1 or row==n or col==1 or col==n or row==col or row+col==n+1:
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print()
'''


#76
'''
        1 
      2 
    3 
      4 
        5 
'''
'''
n=int(input())
space=n-1
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range (1, space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(dummy, end=' ')
    print()
    dummy+=1
    if row<=space:
        space-=1
        
    else:
        space+=1
'''

#77

'''
      1 
    2 
  3 
4 
  5 
    6 
      7
'''

'''
n=int(input())
space=n//2
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range (1, space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(dummy, end=' ')
    print()
    dummy+=1
    if row<n//2+1:
        space-=1
        
    else:
        space+=1
'''


#78
'''
      1 
    3 
  5 
7 
  6 
    4 
      2
'''
'''
n=int(input())
space=n//2
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range (1, space+1):
        print(' ', end=' ')
    for st in range (1, stars+1):
        print(dummy, end=' ')
    print()
    if row<n//2+1:
        space-=1
        dummy+=2
    elif row==n//2+1:
        dummy-=1
        space+=1
    else:
        space+=1
        dummy-=2
'''

#79
'''
      1 
    2 
  3 
4 
  7 
    6 
      5
'''
'''
n=int(input())
space=n//2
stars=1
dummy=1
for row in range (1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print(dummy, end=' ')
    print()
    if row<n//2+1:
        space-=1
        dummy+=1
    elif row==n//2+1:
        space+=1
        dummy=n
    else:
        space+=1
        dummy-=1
'''

#80
'''
      2 
    3 
  5 
7 
  11 
    13 
      17 
'''
'''
n=int(input())
c=0
s=2
l=[]
while True:
    for i in range (2,s//2+1):
        if s%i==0:
            break
    else:
        c+=1
        l.append(s)
        if c==n:
            break     
    s+=1
space=n//2
stars=1
ip=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range (1,stars+1):
        print(l[ip], end=' ')
    print()
    ip+=1
    if row<n//2+1:
        space-=1
    else:
        space+=1
'''


#81.
'''
      2 
    3 
  5 
8 
  13 
    21 
      34 
'''
'''
n=int(input())
SUM=0
n1=1
n2=1
l=[]
for i in range (1,n+1):
    SUM=n1+n2
    n1,n2=n2,SUM
    l.append(SUM)
space=n//2
stars=1
ip=0        
for row in range (1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range (1, stars+1):
        print(l[ip], end=' ')
    print()
    ip+=1
    if row<n//2+1:
        space-=1
    else:
        space+=1
'''

#82.
'''
* * * * * * * 
  * * * * * 
    * * * 
      * 
    * * * 
  * * * * * 
* * * * * * *
'''

'''
n=int(input())
stars=n
space=0
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ', end=' ')
    for st in range (1,stars+1):
        print('*', end=' ')
    print()
    if row<n//2+1:
        stars-=2
        space+=1
    else:
        stars+=2
        space-=1
'''

#83
'''
*       * 
* *     * 
*   *   * 
*     * * 
*       *
'''
'''
n=int(input())
for row in range(1,n+1):
    for col in range (1,n+1):
        if row==col or col==1 or col==n:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''


#84


n=int(input())
dummy=1
i=0
l=[[], [], [] , [] , [] ]
for row in range (1,n+1):
    for col in range (1,n+1):
        l[i].append(dummy)
        dummy+=1    
    i+=1
print(l)

ip=0
for row in range(1,n+1):
    cip=0
    for col in range (1,n+1):
        e=l[ip][cip]
        cip+=1
        print(e, end=' ')
    print()
    ip+=1
    

