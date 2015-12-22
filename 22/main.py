import copy
import sys

class Game:
	def __init__(self, hard_mode = False):
		self.player = Player(name="Player", hp = 50, mana = 500)
		self.boss = Player(name="Boss", hp = 51, damage = 9)
		self.hard_mode = hard_mode

		self.items = list()
		self.items.append(Item(name = "Recharge", mana_cost = 229, rounds = 5, mana_recharge = 101))
		self.items.append(Item(name = "Shield", mana_cost = 113, rounds = 6, armor_increase = 7))
		self.items.append(Item(name = "Drain", mana_cost = 73, damage = 2, heal = 2, instant = True))
		self.items.append(Item(name = "Magic Missile", mana_cost = 53, damage = 4, instant = True))
		self.items.append(Item(name = "Poison", mana_cost = 173, rounds=6, damage = 3))

	def start_game(self):
		self.minimax(copy.deepcopy(self), 0, True)

	def game_ended(self):
		global least_mana_spent

		r = self.player.hp <= 0 or self.boss.hp <= 0
		if r:
			if self.player_won():
				least_mana_spent = min(least_mana_spent, self.player.mana_spent)
		return r

	def player_won(self):
		return self.player.hp > self.boss.hp

	def take_turn(self):
		remove_index = list()

		# player
		for item_index, item in enumerate(self.player.items):
			self.use_item(item, item_index, self.player, self.boss)

			if item.rounds_left == 0:
				remove_index.append(item_index)

		for index in remove_index:
			self.player.armor -= self.player.items[index].armor_increase
			del self.player.items[index]

		# boss, dont have any items

	def use_item(self, item, item_index, p_from, p_to):
		#print("USED ITEM: %s, %s, rounds_left: %d" % (p_from.name, item.name, item.rounds_left))
		p_to.take_damage(item.damage)
		p_from.heal(item.heal)
		p_from.mana += item.mana_recharge

		item.rounds_left -= 1
		
	def cast_item(self, item, item_index, p_from, p_to):
		#print("CAST: %s, %s" % (p_from.name, item.name))
		p_from.mana -= item.mana_cost
		p_from.armor += item.armor_increase
		if item.instant:
			#print("instant use")
			self.use_item(item, item_index, p_from, p_to)
			del p_from.items[item_index]

	# returns item index
	def add_item(self, item, player):
		return player.add_item(item) 

	def item_in_use(self, player, item):
		for p_item in player.items:
			if p_item.name == item.name:
				return True
		return False

	# player = True, boss = False
	def minimax(self, node, depth, players_turn):		
		if node.hard_mode and players_turn:
			node.player.take_damage(1)

		if node.game_ended():
			return 

		if node.player.mana_spent > least_mana_spent:
			return

		# effects
		node.take_turn()

		if node.game_ended():
			return

		if players_turn:
			for item in self.items:
				if node.item_in_use(node.player, item) or item.mana_cost > node.player.mana:
					continue
				node_new = copy.deepcopy(node)
				item_tmp = copy.deepcopy(item)
				item_index = node_new.add_item(item_tmp, node_new.player)
				node_new.cast_item(item_tmp, item_index, node_new.player, node_new.boss)
				self.minimax(node_new, depth+1, not players_turn)
		else: # boss turn
			node_new = copy.deepcopy(node)
			node_new.player.take_damage(node_new.boss.damage)
			self.minimax(node_new, depth+1, not players_turn)


class Player:
	def __init__(self, name = "", hp = 0, damage = 0, armor = 0, mana = 0):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.armor = armor
		self.mana = mana
		self.mana_spent = 0
		self.items = list()

	def add_item(self, item):
		self.items.append(item)
		self.mana_spent += item.mana_cost
		return len(self.items) - 1

	def remove_item(self, item_index):
		del self.items[item_index]

	def take_damage(self, damage):
		self.hp -= max((damage > 0) * 1, damage - self.armor)

	def heal(self, heal):
		self.hp += heal

	def __str__(self):
		return "%s has %d hit points, %d damage, %d armor, %d mana, mana spent: %d" % (self.name, self.hp, self.damage, self.armor, self.mana, self.mana_spent)


class Item:
	def __init__(self, name = "", mana_cost = 0, damage = 0, heal = 0, armor_increase = 0, mana_recharge = 0, rounds = 1, instant = False):
		self.name = name
		self.mana_cost = mana_cost
		self.damage = damage
		self.heal = heal
		self.armor_increase = armor_increase
		self.mana_recharge = mana_recharge
		self.rounds = rounds
		self.rounds_left = rounds
		self.instant = instant

	def __str__(self):
		return "%s got rounds_left: %d" % (self.name, self.rounds_left)


least_mana_spent = sys.maxint
game = Game()
game.start_game()
print("p1", least_mana_spent)

least_mana_spent = sys.maxint
game = Game(hard_mode = True)
game.start_game()
print("p2", least_mana_spent)
