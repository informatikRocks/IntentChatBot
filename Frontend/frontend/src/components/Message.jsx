import React from 'react';
import { motion } from 'framer-motion';
import { User, Bot } from 'lucide-react';

const Message = ({ role, content }) => {
    const isUser = role === 'user';

    return (
        <motion.div
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            className={`w-full py-4 px-4 md:px-8 flex ${isUser ? 'justify-end' : 'justify-start'}`}
        >
            <div className={`flex max-w-3xl gap-4 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>

                {/* Avatar */}
                <div className="flex-shrink-0 flex flex-col justify-end">
                    <div className={`
                        w-10 h-10 rounded-full flex items-center justify-center shadow-lg
                        ${isUser
                            ? 'bg-gradient-to-br from-[var(--color-chat-user-start)] to-[var(--color-chat-user-end)]'
                            : 'bg-white/10 backdrop-blur-md border border-white/10'
                        } 
                    `}>
                        {isUser ? (
                            <User size={18} className="text-white" />
                        ) : (
                            <Bot size={18} className="text-blue-200" />
                        )}
                    </div>
                </div>

                {/* Bubble */}
                <div className={`
                    relative px-6 py-4 shadow-lg text-sm md:text-base leading-relaxed tracking-wide
                    ${isUser
                        ? 'bg-gradient-to-br from-[var(--color-chat-user-start)] to-[var(--color-chat-user-end)] text-white rounded-2xl rounded-tr-sm'
                        : 'bg-[var(--color-chat-bot-bg)] backdrop-blur-md border border-[var(--color-chat-bot-border)] text-[var(--color-chat-text)] rounded-2xl rounded-tl-sm'
                    }
                `}>
                    <div className="prose prose-invert max-w-none">
                        {content.split('\n').map((line, i) => (
                            <p key={i} className={i > 0 ? "mt-2" : "m-0"}>{line}</p>
                        ))}
                    </div>
                </div>
            </div>
        </motion.div>
    );
};

export default Message;