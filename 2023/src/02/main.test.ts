import fs from "fs";
import { describe, expect, it } from "vitest";

const maxCubes = {
  red: 12,
  green: 13,
  blue: 14,
};

function gameIsPossible(game: string) {
  for (const set of game.split(";").map((g) => g.trim())) {
    const cubes = set.split(", ").map((cube) => {
      const [n, color] = cube.split(" ");
      return {
        color,
        value: parseInt(n, 10),
      };
    });

    for (const cube of cubes) {
      // @ts-ignore
      if (cube.value > maxCubes[cube.color]) {
        return false;
      }
    }
  }
  return true;
}

function p1(input: string) {
  let value = 0;

  for (const line of input.split("\n")) {
    const match = line.match(/Game (?<gameNr>\d+): (?<game>.+)/);

    const { gameNr, game } = match?.groups ?? {};

    if (!gameNr || !game) {
      throw new Error("Invalid input");
    }

    value += gameIsPossible(game) ? parseInt(gameNr, 10) : 0;
  }

  return value;
}

function p2(input: string) {
  let powerSum = 0;
  for (const line of input.split("\n")) {
    const match = line.match(/Game (?<gameNr>\d+): (?<game>.+)/);

    const { gameNr, game } = match?.groups ?? {};

    if (!gameNr || !game) {
      throw new Error("Invalid input");
    }

    let tmpMaxCube = {
      red: 0,
      green: 0,
      blue: 0,
    };

    for (const set of game.split(";").map((g) => g.trim())) {
      const cubes = set.split(", ").map((cube) => {
        const [n, color] = cube.split(" ");
        return {
          color,
          value: parseInt(n, 10),
        };
      });

      for (const cube of cubes) {
        tmpMaxCube = {
          red: Math.max(tmpMaxCube.red, cube.color === "red" ? cube.value : 0),
          green: Math.max(
            tmpMaxCube.green,
            cube.color === "green" ? cube.value : 0
          ),
          blue: Math.max(
            tmpMaxCube.blue,
            cube.color === "blue" ? cube.value : 0
          ),
        };
      }
    }
    const power = Object.values(tmpMaxCube).reduce((acc, v) => acc * v, 1);
    powerSum += power;
  }

  return powerSum;
}

describe("2023/02/p1", () => {
  it("example", () => {
    const input = fs.readFileSync("src/02/test.txt", "utf-8");

    expect(p1(input)).toBe(8);
  });

  it("real", () => {
    const input = fs.readFileSync("src/02/input.txt", "utf-8");

    expect(p1(input)).toBe(2776);
  });
});

describe("2023/02/p2", () => {
  it("example", () => {
    const input = fs.readFileSync("src/02/test.txt", "utf-8");

    expect(p2(input)).toBe(2286);
  });

  it("real", () => {
    const input = fs.readFileSync("src/02/input.txt", "utf-8");

    expect(p2(input)).toBe(68638);
  });
});
