

class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		for bracket in s:
			if bracket == '(':
				stack.append(bracket)
			elif bracket == '{':
				stack.append(bracket)
			elif bracket == '[':
				stack.append(bracket)
			else:
				if not stack:
					return False
				top_element = stack.pop()
				if top_element=='(' and bracket == ')':
					continue
				elif top_element=='{' and bracket == '}':
					continue
				elif top_element=='[' and bracket == ']':
					continue
				else:
					return False
		if len(stack) > 0:
			return False
		else:
			return True