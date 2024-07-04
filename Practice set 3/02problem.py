#Write a progam to fill in a letter template given below with name and date.

letter = '''Dear<|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", " Kanhaiya").replace("<|Date|", "04 July 2024"))