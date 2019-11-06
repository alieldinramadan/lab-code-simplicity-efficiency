def my_function(Hypotenuse):
    solutions = [[hypo, adjacent, opposite] for hypo in range(5, Hypotenuse) for adjacent in range(4, Hypotenuse) for opposite in range(3, Hypotenuse) if (hypo*hypo==adjacent*adjacent+opposite*opposite)]
    maximum = 0
    for solution in solutions:
        maximum = max(solution)
    return maximum

Hypotenuse = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(Hypotenuse))))