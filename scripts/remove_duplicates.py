def remove_duplicates(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    return output_list

if __name__ == '__main__':
    # Example usage
    examples = [
        [1, 2, 2, 3, 4, 4, 5],
        ['a', 'b', 'a', 'c', 'b'],
        [],
        [1, 1, 1, 1],
        [1, 'a', 1, 'a']
    ]
    
    for example in examples:
        result = remove_duplicates(example)
        print(f'Input: {example}\nOutput: {result}\n')