input_str = input()
alpha_list = [-1] * 26

for idx, char in enumerate(input_str):
    if alpha_list[ord(char) - ord('a')] == -1:
        alpha_list[ord(char) - ord('a')] = idx

result_str = " ".join(map(str, alpha_list))
print(result_str)
