import time
import sys
import re

def ok_pw_rule_1(s):
	if len(s) < 3:
		return False
	for i in range(3, len(s)):
		a = ord(s[i-2])
		b = ord(s[i-1])
		c = ord(s[i])
		
		if b == a+1 and c == a+2:
			return True
	return False

def ok_pw_rule_3(s):
	p = re.compile(r'.*(.)\1.*(.)\2.*')
	res = re.search(p, s)
	if res:
		return res.group(1) != res.group(2)
	return False

def ok_pw(s):
	return ok_pw_rule_1(s) and ok_pw_rule_3(s)

def incriment_char(s, index=None):
	# base case in recursion
	if index == -1:
		return

	# rule 2
	# reset right
	rr = False
	not_accepted_chars = ['i', 'o', 'l']
	for c in not_accepted_chars:
		if c in s:
			index = s.index(c)
			rr = True

	# if no index, incriment the last char in the string
	s_len = len(s)
	recursion = False
	if index == None:
		index = len(s)-1

	new_char_nr = ord(s[index])+1
	if new_char_nr == 123:
		new_char_nr = ord('a')
		recursion = True

	s_new = ""
	if index == 0:
		s_new = chr(new_char_nr)
		if rr:
			for i in range(len(s[index+1:])):
				s_new += 'a'
		else:
			s_new += s[index+1:]
	elif index == s_len-1:
		s_new = s[:index] + chr(new_char_nr)
	else:
		s_new = s[:index] + chr(new_char_nr)
		if rr:
			for i in range(len(s[index+1:])):
				s_new += 'a'
		else:
			s_new += s[index+1:]

	if recursion:
		return incriment_char(s_new, index-1)

	return s_new

pw = "hxbxwxba"

#sys.exit()

while not ok_pw(pw):
	pw = incriment_char(pw)
print(pw)
pw = incriment_char(pw)

while not ok_pw(pw):
	pw = incriment_char(pw)
print(pw)