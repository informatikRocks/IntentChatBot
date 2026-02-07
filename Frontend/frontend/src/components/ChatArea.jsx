import React, { useState, useRef, useEffect } from 'react';
import { Send, Sparkles, Loader2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import Message from './Message';

const ChatArea = () => {
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const textareaRef = useRef(null);
    const messagesEndRef = useRef(null);

    const [messages, setMessages] = useState([
        { role: 'bot', content: 'Hello! I am your Intent Chatbot. How can I assist you today?' }
    ]);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isLoading]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!input.trim() || isLoading) return;

        const userMessage = input.trim();
        const newMessages = [...messages, { role: 'user', content: userMessage }];
        setMessages(newMessages);
        setInput('');
        setIsLoading(true);

        // Reset textarea height
        if (textareaRef.current) {
            textareaRef.current.style.height = 'auto';
        }

        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage }),
            });

            if (!response.ok) throw new Error('Network response was not ok');

            const data = await response.json();
            setMessages(prev => [...prev, { role: 'bot', content: data.answer }]);

        } catch (error) {
            console.error("Error fetching response:", error);
            setMessages(prev => [...prev, { role: 'bot', content: "Sorry, I encountered a connection error." }]);
        } finally {
            setIsLoading(false);
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
            textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 200)}px`;
        }
    }, [input]);

    return (
        <div className="flex-1 flex flex-col h-full relative overflow-hidden bg-[var(--color-chat-bg)]">

            {/* Messages Scroll Area */}
            <div className="flex-1 overflow-y-auto pb-32 pt-10 scroll-smooth px-4 md:px-0">
                <div className="max-w-3xl mx-auto w-full flex flex-col gap-6">
                    {messages.length === 0 ? (
                        <motion.div
                            initial={{ opacity: 0, scale: 0.9 }}
                            animate={{ opacity: 1, scale: 1 }}
                            className="flex flex-col items-center justify-center py-20 text-[var(--color-chat-text-secondary)]"
                        >
                            <div className="bg-white/5 p-4 rounded-full mb-4 ring-1 ring-white/10">
                                <Sparkles size={48} className="text-blue-400" />
                            </div>
                            <h2 className="text-2xl font-bold text-[var(--color-chat-text)]">Intent Chatbot</h2>
                            <p className="mt-2 text-sm opacity-60">Ready to help you with your queries.</p>
                        </motion.div>
                    ) : (
                        <>
                            {messages.map((msg, idx) => (
                                <Message key={idx} role={msg.role} content={msg.content} />
                            ))}

                            {/* Typing Indicator */}
                            <AnimatePresence>
                                {isLoading && (
                                    <motion.div
                                        initial={{ opacity: 0, y: 10 }}
                                        animate={{ opacity: 1, y: 0 }}
                                        exit={{ opacity: 0, scale: 0.9 }}
                                        className="flex items-center gap-2 ml-4 md:ml-12 mt-2"
                                    >
                                        <div className="bg-[var(--color-chat-bot-bg)] backdrop-blur-md border border-[var(--color-chat-bot-border)] px-4 py-2 rounded-2xl rounded-tl-sm flex items-center gap-1">
                                            <span className="w-1.5 h-1.5 bg-blue-400 rounded-full animate-bounce [animation-delay:-0.3s]"></span>
                                            <span className="w-1.5 h-1.5 bg-blue-400 rounded-full animate-bounce [animation-delay:-0.15s]"></span>
                                            <span className="w-1.5 h-1.5 bg-blue-400 rounded-full animate-bounce"></span>
                                        </div>
                                    </motion.div>
                                )}
                            </AnimatePresence>
                            <div ref={messagesEndRef} />
                        </>
                    )}
                </div>
            </div>

            {/* Input Area */}
            <div className="absolute bottom-6 left-0 w-full px-4 pt-4 z-10">
                <div className="max-w-3xl mx-auto">
                    <motion.div
                        initial={{ y: 20, opacity: 0 }}
                        animate={{ y: 0, opacity: 1 }}
                        className="relative"
                    >
                        <form
                            onSubmit={handleSubmit}
                            className="
                                flex items-end gap-2 
                                bg-[var(--color-chat-input-bg)] 
                                backdrop-blur-xl 
                                border border-[var(--color-chat-border)] 
                                rounded-2xl shadow-2xl 
                                p-2 
                                transition-all duration-300
                                focus-within:ring-2 focus-within:ring-blue-500/30 focus-within:border-blue-500/50
                            "
                        >
                            <textarea
                                ref={textareaRef}
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                onKeyDown={handleKeyDown}
                                placeholder="Message IntentChat..."
                                rows={1}
                                disabled={isLoading}
                                className="
                                    w-full bg-transparent text-[var(--color-chat-text)] 
                                    placeholder-[var(--color-chat-text-secondary)] 
                                    placeholder:opacity-50
                                    focus:outline-none resize-none 
                                    py-3 px-3 max-h-40 overflow-y-auto 
                                    disabled:opacity-50
                                "
                            />
                            <button
                                type="submit"
                                disabled={!input.trim() || isLoading}
                                className={`
                                    p-3 rounded-xl transition-all duration-200 
                                    flex items-center justify-center
                                    ${input.trim() && !isLoading
                                        ? 'bg-gradient-to-r from-blue-600 to-violet-600 text-white shadow-lg hover:shadow-blue-500/25 transform hover:scale-105 active:scale-95'
                                        : 'bg-white/5 text-[var(--color-chat-text-secondary)] cursor-not-allowed'
                                    }
                                `}
                            >
                                {isLoading ? (
                                    <Loader2 className="animate-spin w-5 h-5" />
                                ) : (
                                    <Send className="w-5 h-5 ml-0.5" />
                                )}
                            </button>
                        </form>
                    </motion.div>

                    <div className="text-center text-xs text-[var(--color-chat-text-secondary)] mt-3 opacity-60">
                        IntentChat can make mistakes. Consider checking important information.
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ChatArea;