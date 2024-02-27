input_text = input()
# буква	a	e	i	o	u
# стойност	1	2	3	4	5

vowel_sum = 0
for char in input_text:
    if char == 'a':
        vowel_sum += 1
    elif char == 'e':
        vowel_sum += 2
    elif char == 'i':
        vowel_sum += 3
    elif char == 'o':
        vowel_sum += 4
    elif char == 'u':
         vowel_sum += 5

print(vowel_sum)
