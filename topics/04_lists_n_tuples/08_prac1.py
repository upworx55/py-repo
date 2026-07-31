
# Ask the user to enter names of their 3 favorite movies & store them in a list.

# --- Method1 ----
movies = []

mov1 = input("enter first movie: ")
mov2 = input("enter second movie: ")
mov3 = input("enter third movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# --- Method2 ----
movies1 = []
mov = input("enter 1st movie: ")
movies1.append(mov)
mov = input("enter 2nd movie: ")
movies1.append(mov)
mov = input("enter 3rd movie: ")
movies1.append(mov)

print(movies1)

# --- Method3 ----
movies2 = []
movies2.append(input("enter 1st movie "))
movies2.append(input("enter 2nd movie "))
movies2.append(input("enter 3rd movie "))

print(movies2)
