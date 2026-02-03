import React, { useState, useRef, useEffect } from 'react';
import Message from './Message';

const ChatArea = () => {
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false); // NEU: Loading State
    const textareaRef = useRef(null);

    const [messages, setMessages] = useState([
        { role: 'bot', content: 'Hello! I am your Intent Chatbot. How can I assist you today?' }
    ]);

    // NEU: Die Funktion ist jetzt 'async'
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!input.trim() || isLoading) return; // Verhindert Senden während des Ladens

        const userMessage = input.trim();

        // 1. User Nachricht sofort anzeigen
        const newMessages = [...messages, { role: 'user', content: userMessage }];
        setMessages(newMessages);
        setInput('');
        setIsLoading(true); // Ladezustand aktivieren

        try {
            // 2. Echter Request an dein FastAPI Backend
            // Passe die URL an (z.B. http://localhost:8000/chat)
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                // Das Schema muss zu deinem 'ChatRequest' Pydantic Model passen
                body: JSON.stringify({ message: userMessage }),
            });

            if (!response.ok) {
                throw new Error('Netzwerk-Antwort war nicht ok');
            }

            // 3. Antwort verarbeiten
            const data = await response.json();

            // Das Backend sendet 'ChatResponse(answer=...)', also greifen wir auf data.answer zu
            setMessages(prev => [...prev, { role: 'bot', content: data.answer }]);

        } catch (error) {
            console.error("Fehler beim Abrufen der Antwort:", error);
            setMessages(prev => [...prev, { role: 'bot', content: "Entschuldigung, es gab einen Verbindungsfehler." }]);
        } finally {
            setIsLoading(false); // Ladezustand beenden
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    useEffect(() => {
        if (textareaRef.current) {
            textareaRef.current.style.height = 'auto';
            textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
        }
    }, [input]);

    return (
        <div className="flex-1 flex flex-col h-full relative">
            {/* Messages Scroll Area */}
            <div className="flex-1 overflow-y-auto pb-32 pt-10 scroll-smooth px-4">
                <div className="max-w-3xl mx-auto w-full flex flex-col gap-4">
                    {messages.length === 0 ? (
                        <div className="flex flex-col items-center justify-center py-20 text-chat-text-secondary">
                            {/* ... Dein Placeholder SVG ... */}
                            <h2 className="text-xl font-semibold">Intent Chatbot</h2>
                        </div>
                    ) : (
                        <>
                            {messages.map((msg, idx) => (
                                <Message key={idx} role={msg.role} content={msg.content} />
                            ))}
                            {/* Optional: Lade-Indikator anzeigen */}
                            {isLoading && (
                                <div className="text-chat-text-secondary text-sm ml-2 animate-pulse">
                                    IntentChat schreibt...
                                </div>
                            )}
                        </>
                    )}
                </div>
            </div>

            {/* Input Area */}
            <div className="absolute bottom-0 left-0 w-full bg-gradient-to-t from-chat-bg via-chat-bg to-transparent pb-6 pt-10 px-4">
                <div className="max-w-3xl mx-auto">
                    <form onSubmit={handleSubmit} className="relative flex items-end gap-2 bg-chat-input border border-chat-border rounded-xl shadow-lg p-3 focus-within:ring-1 focus-within:ring-chat-border/50">
                        <textarea
                            ref={textareaRef}
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Message IntentChat..."
                            rows={1}
                            disabled={isLoading} // Input sperren während Request läuft
                            className="w-full bg-transparent text-chat-text placeholder-chat-text-secondary focus:outline-none resize-none py-3 max-h-48 overflow-y-auto disabled:opacity-50"
                        />
                        <button
                            type="submit"
                            disabled={!input.trim() || isLoading}
                            className={`p-2 rounded-lg transition-colors ${input.trim() && !isLoading
                                ? 'bg-chat-user text-white hover:bg-blue-700'
                                : 'bg-transparent text-chat-text-secondary cursor-not-allowed'
                                }`}
                        >
                            {isLoading ? (
                                // Kleiner Spinner oder ... wenn es lädt
                                <span className="animate-spin h-5 w-5 border-2 border-gray-500 border-t-transparent rounded-full block"></span>
                            ) : (
                                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13" /><polygon points="22 2 15 22 11 13 2 9 22 2" /></svg>
                            )}
                        </button>
                    </form>
                    <div className="text-center text-xs text-chat-text-secondary mt-2">
                        IntentChat can make mistakes. Consider checking important information.
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ChatArea;