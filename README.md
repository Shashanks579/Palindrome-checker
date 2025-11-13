It is straightforward, factual, and focuses on the technical implementation described in your report.
Palindrome Checker using Stacks and Queues
This is a Python program that determines if a given string is a palindrome. The implementation specifically utilizes Stack (LIFO) and Queue (FIFO) data structures to perform the check, demonstrating their fundamental properties.
The program is designed to be case-insensitive and ignores all spaces and non-alphanumeric characters.
⚙️ Features
 * Palindrome Detection: Checks if an input string reads the same backward as forward.
 * Input Sanitization: Automatically processes the input string to remove all non-alphanumeric characters (e.g., spaces, punctuation).
 * Case-Insensitive: Converts all characters to lowercase to ensure a consistent comparison.
 * Core DSA Implementation: Uses collections.deque to efficiently implement both:
   * A Stack (LIFO) to retrieve characters in reverse order.
   * A Queue (FIFO) to retrieve characters in their original order.
 * Handles Edge Cases: Correctly identifies empty strings or strings containing no alphanumeric characters as palindromes.
💡 How It Works
The program leverages the opposing properties of stacks and queues to validate the palindrome.
 * Pre-processing: The raw input string is sanitized.All characters are converted to lowercase, and only alphanumeric characters are retained.
 * Populate: The script iterates through the processed string. Each character is simultaneously:
   * Pushed onto a Stack (using append()).
   * Enqueued into a Queue (using append()).
 * Compare: A loop runs as long as the queue is not empty. In each iteration:
   * The first character is removed from the front of the queue (FIFO) using popleft().
   * The last-added character is removed from the top of the stack (LIFO) using pop().
 * Validate: These two characters are compared.If a mismatch is ever found, the function breaks and returns False. If the loop completes without a mismatch, the string is confirmed as a palindrome.
🚀 Usage
Clone the repository and run the script from your terminal:
python palindrome_checker.py

The program will prompt you to enter a string.
Examples
Test Case 1: Complex Palindrome
--- Palindrome Checker using Stack and Queue ---
Enter a string to check: A man, a plan, a canal: Panama
Result: The string "A man, a plan, a canal: Panama" is a palindrome.

Test Case 2: Simple Non-Palindrome
--- Palindrome Checker using Stack and Queue ---
Enter a string to check: python
Result: The string "python" is not a palindrome.

Test Case 3: Empty String
--- Palindrome Checker using Stack and Queue ---
Enter a string to check: 
Result: The string "" is a palindrome.
