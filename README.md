# Full-stack Todo Application

This repository contains a full-stack Todo application with client and server implementations, catering to both mobile and web platforms.

## Client

### Mobile Client (React Native)

The mobile client is built using React Native, allowing users to manage their tasks on the go. It provides an intuitive interface for adding, editing, and completing todos.

#### Setup

To run the mobile client:

1. Navigate to the `client/mobile` directory.
2. Install dependencies: `npm install` or `yarn install`.
3. Start the development server: `npm start` or `yarn start`.
4. Follow the instructions to run the app on an emulator or physical device.

### Web Client (React)

The web client is a React application accessible through desktop browsers. It offers similar functionalities as the mobile client, providing users with a seamless experience across platforms.

#### Setup

To run the web client:

1. Navigate to the `client/web` directory.
2. Install dependencies: `npm install` or `yarn install`.
3. Start the development server: `npm start` or `yarn start`.
4. Open your browser and navigate to the provided URL.

## Server

The server implementations provide the necessary APIs for managing todos. Three different server frameworks are included:

### FastAPI

FastAPI is an asynchronous Python framework known for its high performance and simplicity. It offers a robust RESTful API backend for the Todo application.

#### Setup

To run the FastAPI server:

1. Navigate to the `server/fastapi` directory.
2. Install dependencies: `pip install -r requirements.txt`.
3. Start the server: `uvicorn main:app --reload`.

### Express.js

Express.js is a lightweight Node.js framework widely used for building scalable and efficient APIs. It provides a flexible backend solution for handling todo operations.

#### Setup

To run the Express.js server:

1. Navigate to the `server/express` directory.
2. Install dependencies: `npm install` or `yarn install`.
3. Start the server: `npm start` or `yarn start`.

### Flask

Flask is a Python microframework known for its simplicity and versatility. It offers an easy-to-use backend solution for serving the Todo application's API endpoints.

#### Setup

To run the Flask server:

1. Navigate to the `server/flask` directory.
2. Install dependencies: `pip install -r requirements.txt`.
3. Start the server: `python app.py`.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this Todo application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.