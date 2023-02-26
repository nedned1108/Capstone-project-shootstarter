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
  let pledges;
  let mostPledges;
  if (allProjectsData) {
    projects = Object.values(allProjectsData);
    const backerPerProject = projects.map(project => project.backers)
    mostPledges = projects.find(project => project.backers == Math.max(...backerPerProject))
  }
  if (allPledgesData) pledges = Object.values(allPledgesData);
  
  const totalFund = (array) => {
    let perPledge = array.map(pledge => pledge.price * pledge.users.length)
    let sum = perPledge.reduce((a, b) => {
      return a + b
    }, 0)
    return sum
  }
  const totalPledges = (array) => {
    let userPerPledge = array.map(pledge => pledge.users.length)
    let sum = userPerPledge.reduce((a, b) => {
      return a + b
    }, 0)
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
          <NavLink to={`/project/${mostPledges.id}`}>
            <img src={mostPledges.project_images[0].url}/>
            <h3>{mostPledges.project_name}</h3>
            <p>{mostPledges.description}</p>
          </NavLink>
        </div>
        <div className="recommendedProjectsDiv">
          <h5>RECOMMEND FOR YOU</h5>
          <div className="singleProject">
            <NavLink to={`/project/${projects[1].id}`}>
              <img src={projects[1].project_images[0].url}/>
              <div className="singleProjectInfo">
                <h5>{projects[1].project_name}</h5>
                <p>By {projects[1].owner.first_name} {projects[1].owner.last_name}</p>
              </div>
            </NavLink>
          </div>
        </div>
      </div>
      <div className="allProjects">
        <h2>All Projects</h2>
        {projects.map(project => 
          <NavLink className="allProjectsSingle" to={`/project/${project.id}`}>
            <div className="allProjectsImg">
              <img src={project.project_images[0].url}/>
            </div>
            <div className="allProjectsInfo">
              <h2>{project.project_name}</h2>
              <p>{project.description}</p>
            </div>
          </NavLink>
        )}
      </div>
    </div>
  )
};

export default HomePage;
