import itertools
import sys
import copy

def get_items(l, mini, maxi):
	for i in range(mini, maxi+1):
		if i:
			for item in itertools.combinations(l, i):
				yield [item] if isinstance(item[0], int) else item
		else:
			yield [[0, 0, 0]]

def build_player(player, items):
	for item in items:
		cost, damage, armor = item
		player['cost'] += cost
		player['damage'] += damage
		player['armor'] += armor

def player_won(player, boss):
	while True:
		boss['hp'] -= max(1, player['damage'] - boss['armor'])
		if boss['hp'] <= 0:
			return True
		player['hp'] -= max(1, boss['damage'] - player['armor'])
		if player['hp'] <= 0:
			return False

weapons = [[8,4,0], [10,5,0], [25,6,0], [40,7,0], [74,8,0]]
armors = [[13,0,1], [31,0,2], [53,0,3], [75,0,4], [102,0,5]]
rings = [[25,1,0], [50,2,0], [100,3,0], [20,0,1], [40,0,2], [80,0,3]]

player_origin = {'hp': 100, 'damage': 0, 'armor': 0, 'cost': 0}
boss_origin = {'hp': 103, 'damage': 9, 'armor': 2}

p1 = sys.maxint
p2 = 0
for weapon in get_items(weapons, 1, 1):
	for armor in get_items(armors, 0, 1):
		for ring in get_items(rings, 0, 2):
			
			player = copy.deepcopy(player_origin)
			boss = copy.deepcopy(boss_origin)
			build_player(player, weapon)
			build_player(player, armor)
			build_player(player, ring)

			if player_won(player, boss):
				p1 = min(player['cost'], p1)
			else:
				p2 = max(player['cost'], p2)

print(p1)
print(p2)
