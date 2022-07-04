import * as React from "react";
import "../css/chat.css";

interface ChatProps {
  chatName: string;
  lastMessage: string;
  lastMessageTime: string;
  numberOfUnreadMessages: number;
}

const Chat: React.FunctionComponent<ChatProps> = ({
  chatName,
  lastMessage,
  lastMessageTime,
  numberOfUnreadMessages,
}) => {
  return (
    <div className="chat-container">
      <div className="chat-delimiter">
        <div className="profile-container">
          <img src={require("./profile.jpg")} alt="profile-image" />
        </div>
        <div className="info-container">
          <div className="chatname-container">{chatName}</div>
          <div className="chatmessage-container">
            <p className="message-container">{lastMessage}</p>
            <div className="timemessage-container">{lastMessageTime}</div>
          </div>
        </div>
        <div className="online-container">
          <div className="disk">{numberOfUnreadMessages}</div>
        </div>
      </div>
    </div>
  );
};

export default Chat;
