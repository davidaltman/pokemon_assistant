# Pokémon Assistant

A web application that combines OpenAI's GPT with the PokéAPI to create an interactive Pokémon information assistant. Users can ask questions about any Pokémon and receive detailed, AI-powered responses along with official artwork and statistics.

## Features

- 🤖 AI-powered responses to Pokémon-related questions
- 🖼️ Official Pokémon artwork display
- 📊 Detailed Pokémon statistics (height, weight, types, abilities)
- 💬 Interactive chat interface
- 🔄 Real-time data from PokéAPI

## Tech Stack

- **Backend**
  - FastAPI (Python)
  - OpenAI API
  - PokéAPI

- **Frontend**
  - React
  - CSS3

## Prerequisites

- Python 3.8-3.12
- Node.js 14+
- OpenAI API key

## Environment
This project was developed using Python 3.10.11 and Node.js 20.18.0

It was also tested using Python 3.12 and Node.js 23.0.0

## Installation

### Backend Setup

1. Clone the repository and navigate to the backend directory:
cd backend

2. Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate # On Windows, use .venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file in the backend directory:
OPENAI_API_KEY=your_openai_api_key_here

### Frontend Setup

1. Navigate to the frontend directory:
cd frontend

2. Install dependencies:
npm install

## Running the Application

1. Start the backend server (from the backend directory):
uvicorn app.main:app --reload

2. Start the frontend development server (from the frontend directory):
npm start

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Type your Pokémon-related question in the chat input
2. Questions about specific Pokémon will trigger the display of their information and artwork
3. The AI will provide detailed responses based on the Pokémon's actual data

Example questions:
- "Tell me about Pikachu"
- "What are Charizard's abilities?"
- "Is Bulbasaur good for beginners?"

## Project Structure

```
pokemon-assistant/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── pokemon_service.py
│   │   └── chat_service.py
│   ├── requirements.txt
│   └── .env
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── ChatBox.js
    │   │   └── PokemonDisplay.js
    │   ├── App.js
    │   ├── index.js
    │   └── index.css
    ├── public/
    │   └── index.html
    └── package.json
```

## API Endpoints

- `POST /api/chat`
  - Accepts user messages and returns AI-generated responses
  - Request body: `{ "message": "string" }`

- `GET /api/pokemon/{pokemon_name}`
  - Retrieves detailed information about a specific Pokémon
  - Returns: Pokemon data including name, types, abilities, and sprite URL

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for the GPT API
- [PokéAPI](https://pokeapi.co/) for Pokémon data
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [React](https://reactjs.org/) for the frontend framework

## Contact

David Altman - gautamaltman@gmail.com
Project Link: [https://github.com/davidaltman/pokemon_assistant](https://github.com/davidaltman/pokemon_assistant)
