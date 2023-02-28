import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { thunkLoadAllPledges } from "../../store/pledge";
import { thunkLoadAllProjects } from "../../store/project";
import CreatePledgeModal from "../CreatePledgeModal";
import OpenModalButton from "../OpenModalButton";
import PledgeCard from "../PledgeCard";
import './PledgePage.css'


const PledgePage = () => {
  const dispatch = useDispatch();
  const {projectId} = useParams();
  const allPledgesData = useSelector(state => state.pledge.pledges)
  const currentUser = useSelector(state => state.session.user)
  const projects = useSelector(state => state.project.projects)
  const currentProject = Object.values(projects).find(project => project.id == projectId)

  let pledges;
  if (allPledgesData) {
    pledges = Object.values(allPledgesData).filter(pledge => pledge.project_id == projectId);
  }

  useEffect(() => {
    dispatch(thunkLoadAllPledges())
    dispatch(thunkLoadAllProjects())
  }, [dispatch])

  if (currentProject == undefined) {
    return null
  }

  return (
    <div className="pledgeMainDiv">
      <div className="projectTitle">
        <NavLink to={`/project/${projectId}`}>
          <h2>{currentProject.project_name}</h2>
        </NavLink>
        <p>By {currentProject.owner.first_name} {currentProject.owner.last_name}</p>
      </div>
      <div className="pledgesDiv">
        <h2>Select your reward</h2>
        <div className="addPledge">
          {currentUser && currentProject && currentUser.id == currentProject.owner_id &&
            <OpenModalButton 
              buttonText='Add Pledge'
              modalComponent={<CreatePledgeModal projectId={projectId}/>}
            />
          }
        </div>
        {pledges && pledges.map(pledge => <PledgeCard pledge={pledge} key={pledge.id} />)}
      </div>
    </div>
  )
};

export default PledgePage;
