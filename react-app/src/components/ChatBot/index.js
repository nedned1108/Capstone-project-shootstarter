import React, { useEffect } from "react";

const ChatBot = () => {

  useEffect(() => {
    (function (d, m) {
      let kommunicateSettings = { 
        appId: "35adb62d29787dade80b08e126b234b98", 
        popupWidget: true, 
        automaticChatOpenOnNavigation: true 
      };
      let s = document.createElement("script"); 
      s.type = "text/javascript"; 
      s.async = true;
      s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
      let h = document.getElementsByTagName("head")[0]; 
      h.appendChild(s);
      window.kommunicate = m; 
      m._globals = kommunicateSettings;
    })(document, window.kommunicate || {});
  }, [])

  return (
    <div>
      <h1>Hello</h1>
    </div>
  )
}

export default ChatBot;
