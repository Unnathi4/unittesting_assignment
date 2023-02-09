class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:

        rstr = ''
        i = len(input_str)
        while i > 0:
            rstr += input_str[ i - 1 ]
            i = i - 1
        return rstr


    def find_longest_word(self, sentence: str) -> str:
        
        longest = max(sentence.split(), key=len)
        return longest


    def reverse_list(self, input_list: list) -> list:
        
        return input_list[::-1]




    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        
        count = 0
        for i in input_list:
            if (i == number_to_be_counted):
                count = count + 1
        return count 
