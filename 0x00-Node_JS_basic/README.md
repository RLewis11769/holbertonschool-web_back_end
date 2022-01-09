# NodeJS and ExpressJS

## Important Info

1. Run setup script to install all dependencies for all tasks.

2. Testing directions found in each task description.

3. Main files are stored in main/ directory for organization purposes. Move them to current directory for testing.

4. For 5-8, instead of curling from second terminal, can also view at: http://localhost:1245/students or equivalent URL.

5. Nodemon is set up for task 8 but not previous tasks. Restart the server after any changes.

## Node.js Tasks

### 0-console.js
- displayMessage function that prints string in stdout
- Basic demonstration of how to create/export functions
	- Testing:
		```
		node 0main.js
		```

### 1-stdin.js
- Program that prints "conversation" in stdout based on user input
- Basic demonstration of process.stdin and process.stdout
	- Testing:
		```
		node 1-stdin.js (interactive mode)
		echo "John" | node 1-stdin.js (non-interactive mode)
		```

### 2-read_file.js
- countStudents function that synchronously reads database and prints in stdout
- **Note**: Using asynchronous callbacks is the preferred way to write code in Node to avoid blocking threads
	- Testing:
		```
		node 2-main_1.js (bad database error)
		node 2-main_2.js (correct printing)
		```

### 3-read_file_async.js
- countStudents function that asynchronously reads database, prints in stdout, and returns data
- Helper function used in 5, 7, and 8 (based on return)
- **Note**: Using asynchronous callbacks is the preferred way to write code in Node to avoid blocking threads
	- Testing:
		```
		node 3-main_1.js (bad database error)
		node 3-main_2.js (correct printing)
		```

### 4-http.js
- Basic HTTP server using http module
- Same output for any endpoint
	- First terminal:
		```
		node 4-http.js
		```
	- Second terminal:
		```
		curl localhost:1245 && echo ""
		curl localhost:1245/thistoo && echo ""
		```

### 5-http.js
- More advanced HTTP server using http module
- Prints same content as 3-read_file_async.js in server/second terminal for /students endpoint
	- First terminal:
		```
		node 5-http.js database.csv
		node 5-http.js baddatabase.csv (bad database error after curling)
		```
	- Second terminal:
		```
		curl localhost:1245 && echo ""
		curl localhost:1245/students && echo ""
		```

## Express.js Tasks

### 6-http_express.js
- Basic HTTP server using Express module
- Only / endpoint is set up
	- First terminal:
		```
		node 6-http_express.js
		```
	- Second terminal:
		```
		curl localhost:1245 && echo ""
		curl localhost:1245/error && echo ""
		```

### 7-http_express.js
- More advanced HTTP server using Express module
- Prints same content as 3-read_file_async.js in server/second terminal for /students endpoint
	- First terminal:
		```
		node 7-http_express.js database.csv
		node 7-http_express.js baddatabase.csv (bad database error after curling)
		```
	- Second terminal:
		```
		curl localhost:1245 && echo ""
		curl localhost:1245/students && echo ""
		```

### 8 (full_server)
- Break server, routes, rendering, etc. into different files for organization, maintenance
- **Note**: package.json "dev" script should include `./full_server/server.js` rather than just `./server.js` when starting node from outside of folder (should be set up already)
- **Note**: For bad database error, change package.json script to: `"dev": "nodemon --exec babel-node --presets babel-preset-env ./full_server/server.js ./baddatabase.csv"`
	- utils.js
		- readDatabase helper function for controller functions
		- Import 3-read_file_async.js
	- controllers/
		- AppController.js
			- getHomepage function for homepage rendering
		- StudentsController.js
			- getAllStudents function for /students rendering
			- getAllStudentsByMajor function for /students/any rendering
	- routes/
		- index.js
			- Use express.Router() class to match URLs to controller
	- server.js
		- Create Express server that sets up app and uses routes
	- First terminal:
		```
		npm run dev
		```
	- Second terminal:
		```
		curl localhost:1245 && echo ""
		curl localhost:1245/students && echo ""
		curl localhost:1245/students/CS && echo ""
		curl localhost:1245/students/C && echo "" (hardcoded error message for incorrect endpoint)
		```

## Learning Objectives
- Run javascript using NodeJS
- Use NodeJS modules
- Use specific Node JS module to read files
- Use process to access command line arguments and the environment
- Create a small HTTP server using Node JS
- Create a small HTTP server using Express JS
- Create advanced routes with Express JS
- Use ES6 with Node JS with Babel-node
- Use Nodemon to develop faster
