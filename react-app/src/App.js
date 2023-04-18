import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import HomePage from "./components/HomePage";
import ProjectDetail from "./components/ProjectDetail";
import PledgePage from "./components/PledgePage";
import UserProfilePage from "./components/UserProfilePage";
import Footer from "./components/Footer";
import ChatGPT from "./components/ChatGPT";
import ChatBot from "./components/ChatBot";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/">
            <HomePage />
          </Route>
          <Route exact path="/project/:projectId">
            <ProjectDetail />
          </Route>
          <Route exact path="/project/:projectId/pledge">
            <PledgePage />
          </Route>
          <Route exact path="/profile">
            <UserProfilePage />
          </Route>
        </Switch>
      )}
      <ChatBot />
      {/* <ChatGPT /> */}
      <Footer />
    </>
  );
}

export default App;
