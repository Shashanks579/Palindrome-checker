Import collections
Def is_palindrome(input_string: str) -> bool:
	 “””
	 Checks if a string is a palindrome using a stack and a queue.
 	Args:
	 Input_string: The string to be checked.
 	Returns:
 	True if the string is a palindrome, False otherwise.
 	“””
 	# 1. Pre-process the string: keep only alphanumeric chars and convert to lowercase.
 	Processed_string = ‘’.join(char.lower() for char in input_string if char.isalnum())
 	If not processed_string:
 	# An empty string or a string with no alphanumeric characters is a palindrome.
 		Return True
 	# 2. Populate the data structures.
 	# collections.deque is efficient for appends and pops from both ends.
 	Character_stack = collections.deque()
 	Character_queue = collections.deque()
 	For char in processed_string:
 		# Push to stack (LIFO): append to the right
 		Character_stack.append(char)
	 	# Enqueue to queue (FIFO): append to the right
	 	Character_queue.append(char)
 	# 3. Compare characters by dequeuing from the queue and popping from the stack.
 	Is_match = True
 	While len(character_queue) > 0:
		 # Dequeue from the front (FIFO)
 		Queue_char = character_queue.popleft()
 		# Pop from the top (LIFO)
 		Stack_char = character_stack.pop()
	 	If queue_char != stack_char:
 			Is_match = False
 			Break
 	Return is_match
# Main execution block
If __name__ == “__main__”:
 	Print(“--- Palindrome Checker using Stack and Queue ---“)
 	User_input = input(“Enter a string to check: “)
 If is_palindrome(user_input):
 	Print(f’Result: The string “{user_input}” is a palindrome.’)
 Else:
 	Print(f’Result: The string “{user_input}” is not a palindrome.’)