#test_text = "As I stared at the sign that said step on no pets, I thought to myself damnit, I'm mad, or I'n in a dream, but then something ran past me, was it a cat I saw"

#print(len(test_text.split(' ')))

#can I test for a palindrome
def test_is_palindrome(thing_to_test):
    reverse_word = thing_to_test[::-1]
    print(f"checking {thing_to_test}, reversed is {reverse_word}")
    print(reverse_word == thing_to_test)


#can I format text to be tested for palindeome
def format_for_testing(thing_to_format):
    remove_non_alpha = ''.join(chr for chr in thing_to_format if chr.isalpha())
    return str(remove_non_alpha).replace(' ', '').lower()

#can I iterate through the text_text to find palindromes
test_is_palindrome("tacocat")
test_is_palindrome(("coke"))
test_is_palindrome(format_for_testing("A man, aplan, a canal, Panama!"))