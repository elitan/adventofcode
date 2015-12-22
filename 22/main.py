import copy

class Game:
	def __init__(self):
		self.player = Player(name="Player", hp = 50, mana = 500)
		self.boss = Player(name="Boss", hp = 51, damage = 9)

		self.items = list()
		self.items.append(Item(name = "Magic Missile", mana_cost = 53, damage = 4, instant = True))
		self.items.append(Item(name = "Drain", mana_cost = 73, damage = 2, heal = 2, instant = True))
		self.items.append(Item(name = "Shield", mana_cost = 113, rounds = 6, armor_increase = 7))
		self.items.append(Item(name = "Poison", mana_cost = 173, rounds=6, damage = 3))
		self.items.append(Item(name = "Recharge", mana_cost = 229, rounds = 5, mana_recharge = 101))

	def start_game(self):
		self.minimax(self, 0, True)

	# player = True, boss = False
	def minimax(self, node, depth, players_turn):
		if depth == 3:
			return
		if players_turn:
			print("-- Player turn --")
		else:
			print("-- Boss turn --")
		print(self.player)
		print(self.boss)


		# effects


		if players_turn:
			for item in self.items:
				node = copy.deepcopy(self)

				if node.player.add_item(item): # if instant
				#minimax(node, depth+1, not players_turn)

		else: # boss turn
			self.player.take_damage(self.boss.damage)
			print("Boss attacks for %d damage!" % (self.boss.damage))



class Player:
	def __init__(self, name = "", hp = 0, damage = 0, armor = 0, mana = 0):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.armor = armor
		self.mana = mana

		self.items = list()


	def add_item(self, item):
		if item.instant:
			pass
		else:
			self.items.append(item)
			return False

	def take_damage(self, damage):
		self.hp -= max(1, damage - self.armor)

	def __str__(self):
		return "%s has %d hit points, %d damage, %d armor, %d mana" % (self.name, self.hp, self.damage, self.armor, self.mana)


class Item:
	def __init__(self, name = "", mana_cost = 0, damage = 0, heal = 0, armor_increase = 0, mana_recharge = 0, rounds = 0, instant = False):
		self.name = name
		self.mana_cost = mana_cost
		self.damage = damage
		self.heal = heal
		self.armor_increase = armor_increase
		self.rounds = rounds
		self.rounds_left = rounds
		self.instant = instant


game = Game()
game.start_game()