def read_input() -> str:
  with open('input.txt') as f:
    return f.read().strip()

def part_one(input: str) -> int:
  def total_area(input: str) -> int:
    l, w, h = map(int, input.split('x'))
    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)

    return surface_area + slack
  
  return sum(total_area(line) for line in input.split('\n'))


def part_two(input: str) -> int:
  def total_ribbon(input: str) -> int:
    l, w, h = map(int, input.split('x'))
    perimeter = min(2*(l+w), 2*(l+h), 2*(w+h))
    volume = l*w*h

    return perimeter + volume

  return sum(total_ribbon(line) for line in input.split('\n'))

if __name__ == '__main__':
  input: str = read_input()
  print(part_one(input))
  print(part_two(input))
