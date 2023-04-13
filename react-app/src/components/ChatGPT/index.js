import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getGPT } from "../../store/chatgpt";

const ChatGPT = () => {
  const dispatch = useDispatch();
  const gptKey = useSelector((state) => state.chatGPT.key);
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState([]);
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
      // setAnswer(json.choices[0].text);
    } else {
      setError(true);
    }
    setLoading(false);
  };

  const handleAnswer = (e) => {
    e.preventDefault();
    setAnswer(e.target.value);
  };

  return (
    <div>
      <h1>ChatGPT</h1>
      {loading && <p>Loading...</p>}
      {error && <p>Error</p>}
      {/* <p>{answer}</p> */}
      <form onSubmit={handleSubmit}>
        <ul>
          {messages.map((message, idx) => (
            (idx % 2 === 0) ? 
              <li key={idx} className="gpt-question" style={{ color: "red" }}>
                {message}
              </li>
            :
              <li key={idx} className="gpt-response" style={{ color: "blue" }}>
                {message}
              </li>
          ))}
        </ul>
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
