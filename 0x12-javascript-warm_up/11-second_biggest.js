#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argument = (process.argv.slice(2)).map(Number);
  const sortedargument = argument.sort((a, b) => b - a);
  console.log(sortedargument[1]);
}
