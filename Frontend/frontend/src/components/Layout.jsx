import React, { useState } from 'react';
// Sidebar removed
import ChatArea from './ChatArea';

const Layout = () => {
    return (
        <div className="flex h-screen overflow-hidden bg-chat-bg text-chat-text">
            <ChatArea />
        </div>
    );
};

export default Layout;
