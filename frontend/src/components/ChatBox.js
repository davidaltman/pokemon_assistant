import React, { useState } from 'react';

/**
 * ChatBox component that displays a message history and input field for sending new messages
 * @param {Object} props
 * @param {Array<{type: string, content: string}>} props.messages - Array of message objects containing type and content
 * @param {Function} props.onSendMessage - Callback function to handle sending new messages
 * @returns {JSX.Element} A chat interface component
 */
function ChatBox({ messages, onSendMessage }) {
  const [input, setInput] = useState('');

  /**
   * Handles form submission for sending new messages
   * @param {React.FormEvent} e - Form submission event
   */
  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      onSendMessage(input);
      setInput('');
    }
  };

  return (
    <div className="chat-box">
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.type}`}>
            {msg.content}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about a Pokémon..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default ChatBox;