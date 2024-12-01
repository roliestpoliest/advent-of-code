def read_input() -> str:
  with open('input.txt') as f:
    return f.read().strip()

def part_one(input: str) -> int:
  distance = 0
  
  matrix = [list(map(int, line.split())) for line in input.strip().split('\n')]

  first_index = sorted(pair[0] for pair in matrix)
  second_index = sorted(pair[1] for pair in matrix)

  sorted_matrix = list(zip(first_index, second_index))

  for pair in sorted_matrix:
    distance += abs(pair[0] - pair[1])

  return distance


# def part_two(input: str) -> int:
#   total_similarity = 0
#   matrix = [list(map(int, line.split())) for line in input.strip().split('\n')]

#   for pair in matrix:
#     left = pair[0]
#     similarity = 0 
#     for pair in matrix:
#       right = pair[1]
#       if left == right:
#         similarity += 1

#     total_similarity += (left * similarity)

#   return total_similarity

def part_two(input: str) -> int:
  # Parse input into a matrix
  matrix = [list(map(int, line.split())) for line in input.strip().split('\n')]

  # Step 1: Count occurrences of each element in the second column
  second_column_count = {}
  for pair in matrix:
    right = pair[1]
    second_column_count[right] = second_column_count.get(right, 0) + 1

  # Step 2: Compute total similarity
  total_similarity = 0
  for pair in matrix:
    left = pair[0]
    similarity = second_column_count.get(left, 0)  # Get count of `left` in second column
    total_similarity += (left * similarity)

  return total_similarity

if __name__ == '__main__':
  input: str = read_input()

  print(part_one(input))
  print(part_two(input))
