#include <stdio.h>
#include <stdlib.h>

void print_players(int players[], int players_n) {
	for (int i = 0; i < players_n; i++) {
		printf("%d, ", players[i]);
	}
	printf("\n");
}

int next_player_alive(int current_position, int players[], int players_n) {
	int i = current_position;

	while (1) {
		i = (i + 1) % players_n;
		if (!players[i]) {
			return i;
		}
	}
}

void kill_player(int current_position, int players_alive, int players[], int players_n) {
	int killed = 0;
	int i = current_position;
	int stepped_players = 0;

	while (stepped_players < (players_alive / 2)) {
		i = (i + 1) % players_n;
		if(!players[i]) {
			stepped_players++;
		}
	}

	players[i] = 1;
}

int main() {
	// int players_n = 5;
	int players_n = 3001330;
	int* players = malloc(players_n * sizeof(int));
	int dead_players = 0;
	int current_player = 0; // (index)

	// init all to 0
	for (int i = 0; i < players_n; i++) {
		players[i] = 0;
	}

	while (dead_players < (players_n - 1)) {

		kill_player(current_player, (players_n - dead_players), players, players_n);
		current_player = next_player_alive(current_player, players, players_n);
		dead_players++;
		printf("players left: %d\n", (players_n - dead_players));
	}

	printf("%d\n", (current_player + 1));

	free(players);
	return 0;
}
