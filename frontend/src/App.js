import React, { useState } from 'react';
import ChatBox from './components/ChatBox';
import PokemonDisplay from './components/PokemonDisplay';

/**
 * Main application component for the Pokémon Assistant.
 * Manages chat messages and Pokémon data state, handles communication with backend API.
 * @component
 * @returns {JSX.Element} The rendered App component
 */
function App() {
  const [messages, setMessages] = useState([]);
  const [pokemonData, setPokemonData] = useState(null);

  /**
   * Handles sending messages to the chat API and processes Pokemon-related queries.
   * @param {string} message - The message sent by the user
   * @returns {Promise<void>}
   */
  const handleSendMessage = async (message) => {
    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();

      setMessages(prev => [...prev,
        { type: 'user', content: message },
        { type: 'assistant', content: data.response }
      ]);

      // Use AI to find and correct Pokemon names in the message
      const pokemonResponse = await fetch('http://localhost:8000/api/pokemon-from-message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      const pokemonData = await pokemonResponse.json();
      if (!pokemonData.error) {
        setPokemonData(pokemonData);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Pokémon Assistant</h1>
      </header>
      <main className="App-main">
        <div className="chat-container">
          <ChatBox messages={messages} onSendMessage={handleSendMessage} />
        </div>
        {pokemonData && (
          <div className="pokemon-container">
            <PokemonDisplay pokemon={pokemonData} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;