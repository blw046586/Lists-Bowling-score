import sys

# Read input
data = list(map(int, sys.stdin.read().split()))
num_throws = data[0]
throws = data[1:]

frame_scores = [0] * 10
throw_index = 0

# Frames 1 to 9
for i in range(9):
    if throws[throw_index] == 10:  # Strike
        frame_scores[i] = 10 + throws[throw_index + 1] + throws[throw_index + 2]
        throw_index += 1
    elif throws[throw_index] + throws[throw_index + 1] == 10:  # Spare
        frame_scores[i] = 10 + throws[throw_index + 2]
        throw_index += 2
    else:  # Open
        frame_scores[i] = throws[throw_index] + throws[throw_index + 1]
        throw_index += 2

# Frame 10
frame_scores[9] = sum(throws[throw_index:])

# Accumulate scores
for i in range(1, 10):
    frame_scores[i] += frame_scores[i - 1]

# Output with trailing space
print(" ".join(map(str, frame_scores)) + " ")
