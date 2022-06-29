import * as React from "react";
import FriendsList from "./frindslist";
import Menu from "./menu";
import WebBrowser from "./webbrowser";
import "../css/layout.css";

interface LayOutProps {}

const LayOut: React.FunctionComponent<LayOutProps> = () => {
  return (
    <div className="layout-container">
      <Menu />
      <div className="web-container">
        <FriendsList />
        <WebBrowser />
      </div>
    </div>
  );
};

export default LayOut;
