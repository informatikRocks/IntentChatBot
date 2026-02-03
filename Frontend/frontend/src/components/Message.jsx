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
                        ${isUser ? 'bg-chat-user' : 'bg-black'} 
                    `}>
                        {/* ^^^ HIER GEÄNDERT: 'bg-black' statt 'bg-emerald-600' */}

                        {isUser ? (
                            // User Icon (Dein SVG)
                            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                <circle cx="12" cy="7" r="4"></circle>
                            </svg>
                        ) : (
                            // Bot Icon (Der weiße Punkt)
                            <div className="w-3 h-3 bg-white rounded-full"></div>
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