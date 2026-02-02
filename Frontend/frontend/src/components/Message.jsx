import React from 'react';

const Message = ({ role, content }) => {
    const isUser = role === 'user';

    return (
        <div className={`w-full py-2 px-4 md:px-6 flex ${isUser ? 'justify-end' : 'justify-start'}`}>
            <div className={`flex max-w-3xl gap-3 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>

                {/* Avatar */}
                <div className="flex-shrink-0 flex flex-col justify-end">
                    <div className={`
                        w-8 h-8 rounded-full flex items-center justify-center shadow-md
                        ${isUser ? 'bg-chat-user' : 'bg-emerald-600'}
                    `}>
                        {isUser ? (
                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                <circle cx="12" cy="7" r="4"></circle>
                            </svg>
                        ) : (
                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                <path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V11h-2V5.73A2.002 2.002 0 0 1 12 2Z"></path>
                                <path d="M12 13a2 2 0 0 1 2 2v2h-4v-2c0-1.1.9-2 2-2Z"></path>
                                <path d="M12 19a2 2 0 0 1 2 2v1h-4v-1c0-1.1.9-2 2-2Z"></path>
                                <path d="M7.74 13.97a3 3 0 0 1 2.26-4.97V11h2V9a3 3 0 0 1 5 2.24"></path>
                            </svg>
                        )}
                    </div>
                </div>

                {/* Bubble */}
                <div className={`
                    relative px-5 py-3 shadow-sm text-sm md:text-base leading-relaxed
                    ${isUser
                        ? 'bg-chat-user text-white rounded-2xl rounded-tr-sm'
                        : 'bg-chat-bot text-chat-text rounded-2xl rounded-tl-sm border border-chat-border/50'
                    }
                `}>
                    <div className="prose prose-invert max-w-none">
                        {content.split('\n').map((line, i) => (
                            <p key={i} className={i > 0 ? "mt-2" : "m-0"}>{line}</p>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Message;
