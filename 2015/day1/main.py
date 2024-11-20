def read_input() -> str:
  with open('input.txt') as f:
    return f.read().strip()

def part_one(input: str) -> int:
  return input.count('(') - input.count(')')

def part_two(input: str) -> int:
  for i, c in enumerate(input):
    if part_one(input[:i+1]) == -1:
      return i + 1

if __name__ == '__main__':
  input: str = read_input()
  print(part_one(input))
  print(part_two(input))
