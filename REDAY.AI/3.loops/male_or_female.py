def male_or_female(g):
    if g  == 'M' or g == 'm':
        return "Male"
    elif g  == 'F' or g == 'f':
        return "Female"
    else:
        return "not identifiable"



gender = str(input("Enter a M/F: "))

result = male_or_female(gender)
print(f"The person is {result}.")
