// When user inputs name, print message with name
// When user ends program, print message
// Note: process.stdin returns stream connected to stdin as net.Socket
console.log('Welcome to Holberton School, what is your name?');

process.stdin
  // Reads data from stdin, saves to variable, and prints
  .on('readable', () => {
    const name = process.stdin.read();
    if (name !== null) {
      process.stdout.write(`Your name is: ${name}`);
    }
  })
  // When used interactively, program ends when user presses Ctrl+D
  // But if typing readable data, never "ends" and doesn't hit below
  // When used non-interactively, program will end when hits EOF
  .on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
