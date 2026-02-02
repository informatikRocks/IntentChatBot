import React from 'react';

const Sidebar = ({ isOpen, toggleSidebar }) => {
    return (
        <>
            {/* Mobile overlay */}
            {isOpen && (
                <div
                    className="fixed inset-0 bg-black/50 z-20 md:hidden transition-opacity"
                    onClick={toggleSidebar}
                />
            )}

            {/* Sidebar */}
            <div className={`
        fixed md:static inset-y-0 left-0 z-30
        w-64 bg-chat-sidebar border-r border-chat-border
        transform transition-transform duration-300 ease-in-out
        ${isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
        flex flex-col
      `}>
                <div className="p-4 border-b border-chat-border flex items-center gap-2">
                    <div className="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center">
                        <span className="text-white font-bold">AI</span>
                    </div>
                    <h1 className="font-semibold text-lg text-white">IntentChat</h1>
                </div>

                <div className="flex-1 overflow-y-auto p-2 space-y-1">
                    <div className="px-3 py-2 text-xs font-semibold text-chat-text-secondary uppercase tracking-wider">
                        Today
                    </div>

                    {/* Mock History Items */}
                    {['Project Planning', 'React Components', 'Tailwind Config'].map((item, index) => (
                        <button
                            key={index}
                            className="w-full text-left px-3 py-2 rounded-lg hover:bg-chat-bot text-sm text-chat-text transition-colors truncate"
                        >
                            {item}
                        </button>
                    ))}
                </div>

                <div className="p-4 border-t border-chat-border">
                    <button className="flex items-center gap-3 w-full px-3 py-2 rounded-lg hover:bg-chat-bot text-sm text-chat-text transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                        <span>User Profile</span>
                    </button>
                </div>
            </div>
        </>
    );
};

export default Sidebar;
