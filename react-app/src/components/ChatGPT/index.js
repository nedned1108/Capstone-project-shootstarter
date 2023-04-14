import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getGPT } from "../../store/chatgpt";
import "./ChatGPT.css";

const ChatGPT = () => {
  const dispatch = useDispatch();
  const gptKey = useSelector((state) => state.chatGPT.key);
  const [message, setMessage] = useState("");
  const [visible, setVisible] = useState(true);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const apiUrl = "https://api.openai.com/v1/engines/davinci/completions";

  useEffect(async () => {
    await dispatch(getGPT());
  }, [dispatch]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(false);
    const data = {
      prompt: message,
      max_tokens: 20,
      temperature: 0.7,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
      stop: ["\ { "],

    };
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${gptKey}`,
      },
      body: JSON.stringify(data),
    });
    const json = await response.json();
    console.log(json)
    if (json.choices) {
      setMessages([...messages, message, json.choices[0].text]);
      setMessage("");
    } else {
      setError(true);
    }
    setLoading(false);
  };

  const hideChat = () => {
    setVisible(false);
  };
  const showChat = () => {
    setVisible(true);
  };

  return (
      <div>
        <h1>AI Assistant</h1>
        <form onSubmit={handleSubmit}>
          <div className="chatBox" >
            {loading && <p>Loading...</p>}
            {error && <p>Error</p>}
            {messages.map((message, idx) => (
              (idx % 2 === 0) ? 
                <div key={idx} className="gpt-question" >
                  <div className="question-inner" >
                    {message}
                  </div>
                </div>
              :
                <div key={idx} className="gpt-response" >
                  <div className="response-inner" > 
                    {message}
                  </div>
                </div>
            ))}
          </div>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            required
          />
          <button type="submit">Submit</button>
        </form>
      </div>
  )
}

export default ChatGPT;
