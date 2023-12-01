import fs from "fs";

async function main() {
  const file = fs.readFileSync("src/01/input.txt", "utf-8");

  let sum = 0;

  for (const line of file.split("\n")) {
    const digits = line.replace(/[^\d.-]+/g, "");

    const a = digits.substring(0, 1);
    const b = digits.substring(digits.length - 1);

    sum += parseInt(`${a}${b}`);
  }

  console.log(sum);
}

main();
