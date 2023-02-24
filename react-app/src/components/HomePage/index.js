//react-app/src/components/HomePage/index.js
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkLoadAllProjects } from "../../store/project";
import { thunkLoadAllPledges } from "../../store/pledge";
import { NavLink } from "react-router-dom";
import "./HomePage.css";


const HomePage = () => {
  const dispatch = useDispatch();
  const allProjectsData = useSelector(state => state.project.projects)
  const allPledgesData = useSelector(state => state.pledge.pledges)
  let projects;
  let pledges
  if (allProjectsData) projects = Object.values(allProjectsData);
  if (allPledgesData) pledges = Object.values(allPledgesData);
  
  const totalFund = (array) => {
    let perPledge = array.map(pledge => pledge.price * pledge.users.length)
    let sum = perPledge.reduce((a, b) => {
      return a + b
    }, perPledge[0])
    return sum
  }
  const totalPledges = (array) => {
    let userPerPledge = array.map(pledge => pledge.users.length)
    let sum = userPerPledge.reduce((a, b) => {
      return a + b
    }, userPerPledge[0])
    return sum
  }

  useEffect(() => {
    dispatch(thunkLoadAllProjects())
    dispatch(thunkLoadAllPledges())
  }, [dispatch])

  if (projects.length == 0 && pledges.length == 0) {
    return null
  }
  
  return (
    <div className="mainDiv">
      <h1>Bring a creative project to life.</h1>
      <h5>ON SHOOTSTARTER:</h5>
      <div className="onShootstarter">
        <div>
          <h2>{projects.length}</h2>
          <p>projects funded</p>
        </div>
        <div>
          <h2>${totalFund(pledges)}</h2>
          <p>towards creative work</p>
        </div>
        <div>
          <h2>{totalPledges(pledges)}</h2>
          <p>pledges</p>
        </div>
      </div>
      <div className="projectsDiv">
        <div className="mainProject">
          <h5>FEATURED PROJECT</h5>
          <NavLink to={`/project/${projects[0].id}`}>
            <img src={projects[0].project_images[0].url}/>
            <h3>{projects[0].project_name}</h3>
          </NavLink>
        </div>
        <div className="recommendedProjectsDiv">
          <h5>RECOMMEND FOR YOU</h5>
          <div className="singleProject">
            <NavLink to={`/project/${projects[1].id}`}>
              <img src={projects[1].project_images[0].url}/>
              <h5>{projects[1].project_name}</h5>
            </NavLink>
          </div>
        </div>
      </div>
    </div>
  )
};

export default HomePage;
