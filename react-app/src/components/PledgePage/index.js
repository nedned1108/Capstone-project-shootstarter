import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { thunkLoadAllPledges } from "../../store/pledge";
import { thunkLoadAllProjects } from "../../store/project";
import CreatePledgeModal from "../CreatePledgeModal";
import OpenModalButton from "../OpenModalButton";
import PledgeCard from "../PledgeCard";


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

  if (pledges.length == 0 && !currentProject) {
    return null
  }

  return (
    <div>
      <div>
        {currentUser && currentUser.id == currentProject.owner_id ?
          <OpenModalButton 
            buttonText='Add Pledge'
            modalComponent={<CreatePledgeModal projectId={projectId}/>}
          />
          : ''
        }
      </div>
      <div>
        <h2>Select your reward</h2>
        {pledges.map(pledge => <PledgeCard pledge={pledge} key={pledge.id} />)}
      </div>
    </div>
  )
};

export default PledgePage;
