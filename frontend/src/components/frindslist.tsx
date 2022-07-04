import * as React from "react";
import Chat from "./chat";
import "../css/friendslist.css";

interface FriendsListProps {}

const FriendsList: React.FunctionComponent<FriendsListProps> = () => {
  React.useEffect(() => {
    /**
     * API Calls to the server to get data:
     * -get the number of chats opened for this account
     * -for each chat, get the name of the chat (if it has no name, use the other person's name),
     * -get the last message and the time when it was sent
     * -get the number of unread messages in the chat for this person
     * -store them into variables and / or states
     */
  });

  return (
    <div className="friendslist-container">
      <Chat
        chatName="Paul Nafureanu"
        lastMessage="Hello message from our workers.." //Need to be cut before sended
        lastMessageTime="12m"
        numberOfUnreadMessages={3}
      />
      <Chat
        chatName="Adi Granescu"
        lastMessage="Helloooo, message from our.."
        lastMessageTime="5m"
        numberOfUnreadMessages={1}
      />
    </div>
  );
};

export default FriendsList;
