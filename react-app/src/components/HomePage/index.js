//react-app/src/components/HomePage/index.js
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkLoadAllProjects } from "../../store/project";
import { NavLink } from "react-router-dom";
import "./HomePage.css";


const HomePage = () => {
  const dispatch = useDispatch();
  const allProjectsData = useSelector(state => state.project.projects)
  let projects;
  if (allProjectsData) projects = Object.values(allProjectsData);
  useEffect(() => {
    dispatch(thunkLoadAllProjects())
  }, [dispatch])

  if (projects.length == 0) {
    return null
  }
  
  return (
    <div>
      <h1>Bring a creative project to life.</h1>
      <h5>ON SHOOTSTARTER:</h5>
      <div>
        <div>projects funded</div>
        <div>towards creative work</div>
        <div>pledges</div>
      </div>
      <div>
        <div>
          <NavLink to={`/project/${projects[0].id}`}>
            <img src={projects[0].project_images[0].url}/>
            <h3>{projects[0].project_name}</h3>
          </NavLink>
        </div>
      </div>
    </div>
  )
};

export default HomePage;