import fs from "fs";

function isCharANumber(char: string) {
  return /^\d$/.test(char);
}

async function main() {
  const file = fs.readFileSync("src/01/input.txt", "utf-8");

  const nrMap = {
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  let sum = 0;

  for (const line of file.split("\n")) {
    let newLine = "";

    for (const [i, char] of line.split("").entries()) {
      if (isCharANumber(char)) {
        newLine += char;
      }

      for (const [word, nr] of Object.entries(nrMap)) {
        if (line.substring(i, i + word.length) === word) {
          newLine += nr;
        }
      }
    }

    const digits = newLine.replace(/[^\d.-]+/g, "");

    const a = digits.substring(0, 1);
    const b = digits.substring(digits.length - 1);

    sum += parseInt(`${a}${b}`);
  }

  console.log(sum);
}

main();
