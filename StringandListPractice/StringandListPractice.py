# replace day in first sentence with month
words = "It's thanksgiving day. It's my birthday, too!"
words.find(" day")
words.replace(" day", " month")
print words

x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

y = ["hello", 2, 54, -2, 7, 12, 98, "world"]
newY = y[1:8]
print newY
print y

z = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]  # Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
z.sort()
print z
