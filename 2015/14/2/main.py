import re
import sys

def move_reindeers(reindeers):
	for i, reindeer in enumerate(reindeers):
		speed, speed_s, rest_s, flying, seconds_left, distance, points = reindeer
		if flying:
			distance += speed

		seconds_left -= 1

		if seconds_left == 0:
			flying = not flying
			seconds_left = speed_s if flying else rest_s

		reindeers[i] = [speed, speed_s, rest_s, flying, seconds_left, distance, points]

def extra_point_to_leaders(reindeers):
	leader_distance = 0
	for i, reindeer in enumerate(reindeers):
		if reindeer[-2] > leader_distance:
			leader_distance = reindeer[-2]

	for reindeer in reindeers:
		if reindeer[-2] == leader_distance:
			reindeer[-1] = reindeer[-1] + 1


reindeers = list()

with open('input') as f:
	longest_distance = 0
	for line in f:
		line = line.rstrip()

		speed, speed_s, rest_s = map(int, re.findall(ur'(?:\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)[0])

		# speed, speed_s, rest_s, flying, seconds_left, distance, points
		reindeers.append([speed, speed_s, rest_s, True, speed_s, 0, 0])



i, distance = 0, 0 
flying = True
seconds_left = speed_s
for i in range(2503):
	move_reindeers(reindeers)
	extra_point_to_leaders(reindeers)

highest_points = 0
for r in reindeers:
	if r[-1] > highest_points:
		highest_points = r[-1]

print(highest_points)