# ex 1
import re

def match_pat(s):
    pattern = r'^ab*$'
    if re.match(pattern, s):
        return True
    else:
        return False

test_str = ['a', 'ab', 'abb', 'abbbb', 'b', 'bbb']
for test in test_str:
    print(f"{test}: {match_pat(test)}")

# ex 2
import re

def match_pat(s):
    pattern = r'^ab{2,3}$'
    if re.match(pattern, s):
        return True
    else:
        return False
test_str = ['a', 'ab', 'abb', 'abbb', 'abbbb', 'b']
for x in test_str:
    print(f"{x}: {match_pat(x)}") 

# ex 3
import re

def find_seq(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    seq = re.findall(pattern, text)
    return seq

text = "This is a test_text for finding sequences like this_one or that_two."
found_seq = find_seq(text)
print("Found sequences:", found_seq)

# ex 4
import re

def find_seq(txt):
    pattern = r'\b[A-Z][a-z]+\b'
    seq = re.findall(pattern, txt)
    return seq

text = "This is a Test string With Multiple Sequences Like This One and That Two"
found_seq = find_seq(text)
print("Found sequences:", found_seq)

# ex 5
import re

def match_pat(s):
    pattern = r'^a.*b$'
    if re.match(pattern, s):
        return True
    else:
        return False

strr = ['ab', 'acd', 'axxxxxb', 'a_b', 'a', 'b']
for x in strr:
    print(f"{x}: {match_pat(x)}")

# ex 6
import re

def rep(txt):
    return txt.replace(' ', ':').replace(',', ':').replace('.', ':')

text = "This is a test, for replacing spaces. And commas, with colons."
res = rep(text)
print("Original text:", text)
print("Modified text:", res)

# ex 7
def snake_camel(snake):
    words = snake.split('_')
    camel = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel

snake_str = "snake_case_example_string"
camel_str = snake_camel(snake_str)
print("Original string:", snake_str)
print("Converted string:", camel_str)

# ex 8
import re

def spl_upp(s):
    return re.findall('[A-Z][^A-Z]*', s)

user_str = str(input())
res = spl_upp(user_str)
print("Original string:", user_str)
print("Split result:", res)

# ex 9
import re

def ins(txt):
    modified = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
    return modified

user_str = str(input())
res = ins(user_str)
print("Original string:", user_str)
print("Modified string:", res)

# ex 10
def camel_to_snake(camel_case):
    snake_case = ''
    for x in camel_case:
        if x.isupper():
            snake_case += '_' + x.lower()
        else:
            snake_case += x

    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

camel_str = str(input())
snake_str = camel_to_snake(camel_str)
print("Original string:", camel_str)
print("Converted string:", snake_str)