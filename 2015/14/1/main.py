import re

with open('input') as f:
	longest_distance = 0
	for line in f:
		line = line.rstrip()

		speed, speed_s, rest_s = map(int, re.findall(ur'(?:\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)[0])

		i, distance = 0, 0 
		flying = True
		seconds_left = speed_s
		while i < 2503:
			if flying:
				distance += speed

			seconds_left -= 1

			if seconds_left == 0:
				flying = not flying
				seconds_left = speed_s if flying else rest_s

			print(i, distance)
			i += 1

		if distance > longest_distance:
			longest_distance = distance

print(longest_distance)