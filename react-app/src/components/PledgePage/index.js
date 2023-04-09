import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { thunkLoadAllPledges } from "../../store/pledge";
import { thunkLoadAllProjects } from "../../store/project";
import { thunkLoadAllPayments } from "../../store/payment_method"
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
  const payment_methodsData = useSelector(state => state.payment.payments)
  const currentProject = Object.values(projects).find(project => project.id == projectId)
  let daysToGo
  let today = new Date()
  if (currentProject) {
    const oneDay = 1000*60*60*24;
    const endDay = new Date(currentProject.end_day.split('-').join('/'))
    daysToGo = Math.ceil((endDay.getTime() - today.getTime())/oneDay)
  }

  let pledges;
  if (allPledgesData) {
    pledges = Object.values(allPledgesData).filter(pledge => pledge.project_id == projectId);
  }
  let payment_methods;
  if (payment_methodsData) {
    payment_methods = Object.values(payment_methodsData)
  }

  useEffect(() => {
    dispatch(thunkLoadAllPledges())
    dispatch(thunkLoadAllProjects())
    dispatch(thunkLoadAllPayments())
  }, [dispatch])

  if (currentProject == undefined || payment_methods == undefined) {
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
        <div>
          <h2>Select your reward</h2>
          <p>You can only choose each reward once</p>
        </div>
        <div className="addPledge">
          {currentUser && currentProject && currentUser.id == currentProject.owner_id &&
            <OpenModalButton 
              buttonText='Add Pledge'
              modalComponent={<CreatePledgeModal projectId={projectId}/>}
            />
          }
        </div>
        {pledges && pledges.map(pledge => <PledgeCard pledge={pledge} payment_methods={payment_methods} daysToGo={daysToGo} key={pledge.id} />)}
      </div>
    </div>
  )
};

export default PledgePage;
