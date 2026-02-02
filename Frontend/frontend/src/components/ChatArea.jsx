import React, { useState, useRef, useEffect } from 'react';
import Message from './Message';

const ChatArea = () => {
    const [input, setInput] = useState('');
    const textareaRef = useRef(null);

    // Mock Messages
    const [messages, setMessages] = useState([
        { role: 'bot', content: 'Hello! I am your Intent Chatbot. How can I assist you today?' }
    ]);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!input.trim()) return;

        // Add user message
        const newMessages = [...messages, { role: 'user', content: input }];
        setMessages(newMessages);
        setInput('');

        // Simulate bot response
        setTimeout(() => {
            setMessages(prev => [...prev, { role: 'bot', content: 'This is a simulated response. The backend is not connected yet.' }]);
        }, 1000);
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    // Auto-resize textarea
    useEffect(() => {
        if (textareaRef.current) {
            textareaRef.current.style.height = 'auto';
            textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
        }
    }, [input]);

    return (
        <div className="flex-1 flex flex-col h-full relative">

            {/* Messages Scroll Area */}
            {/* Messages Scroll Area */}
            <div className="flex-1 overflow-y-auto pb-32 pt-10 scroll-smooth px-4">
                <div className="max-w-3xl mx-auto w-full flex flex-col gap-4">
                    {messages.length === 0 ? (
                        <div className="flex flex-col items-center justify-center py-20 text-chat-text-secondary">
                            <div className="w-16 h-16 bg-chat-input rounded-full flex items-center justify-center mb-4">
                                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10" /><path d="M12 16v-4" /><path d="M12 8h.01" /></svg>
                            </div>
                            <h2 className="text-xl font-semibold">Intent Chatbot</h2>
                        </div>
                    ) : (
                        messages.map((msg, idx) => (
                            <Message key={idx} role={msg.role} content={msg.content} />
                        ))
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
                            className="w-full bg-transparent text-chat-text placeholder-chat-text-secondary focus:outline-none resize-none py-3 max-h-48 overflow-y-auto"
                        />
                        <button
                            type="submit"
                            disabled={!input.trim()}
                            className={`p-2 rounded-lg transition-colors ${input.trim()
                                ? 'bg-chat-user text-white hover:bg-blue-700'
                                : 'bg-transparent text-chat-text-secondary cursor-not-allowed'
                                }`}
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13" /><polygon points="22 2 15 22 11 13 2 9 22 2" /></svg>
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
