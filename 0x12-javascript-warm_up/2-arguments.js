#!/usr/bin/node
// Prints a message depending on the number of arguments passed

// process.argv contains an array of command-line arguments passed to the script
const argsCount = process.argv.length - 2; // Subtract 2 to exclude 'node' and script path

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

