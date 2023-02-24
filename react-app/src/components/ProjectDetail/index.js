import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { thunkLoadAllProjects } from "../../store/project";
import { thunkDeleteProject } from "../../store/project";
import UpdateProjectModal from "../UpdateProjectModal";
import OpenModalButton from "../OpenModalButton";
import './ProjectDetail.css'


const ProjectDetail = () => {
  const { projectId } = useParams();
  const dispatch = useDispatch();
  const history = useHistory();
  const projects = useSelector(state => state.project.projects)
  const currentProject = Object.values(projects).find(project => project.id == projectId)
  const currentUser = useSelector(state => state.session.user)

  useEffect(() => {
    dispatch(thunkLoadAllProjects())
  }, [dispatch, projectId])
  const deleteProject = (e) => {
    dispatch(thunkDeleteProject(e))
    history.push('/')
    return 
  }

  if (!currentProject) {
    return null
  }

  return (
    <div className="projectMainDiv">
      <div className="projectTitle">
        <h2>{currentProject.project_name}</h2>
        <h3>{currentProject.description}</h3>
      </div>
      <div className="projectImgInfo">
        <div className="projectImg">
          <img src={currentProject.project_images[0].url}/>
        </div>
        <div className="projectInfo">
          <div className="projectInfoNum">
            <h4 className="currentFund">${currentProject.current_fund}</h4>
            <p>pledged of ${currentProject.goal}</p>
            <h4>{currentProject.backers}</h4>
            <p>backers</p>
            <h4>{currentProject.end_day}</h4>
            <div className="pledgeButton">
              <NavLink to={`/project/${currentProject.id}/pledge`}>
                Back this project
              </NavLink>
            </div>
            {currentUser && currentUser.id == currentProject.owner_id ? 
            <div className="editDelete">
              <OpenModalButton 
                buttonText="Update Project"
                modalComponent={<UpdateProjectModal project={currentProject}/>}
              />
              <button onClick={() => deleteProject(currentProject.id)}>Delete Project</button>
            </div>
            : '' 
            } 
          </div>
        </div>
      </div>
      <div>
        <div>{currentProject.story}</div>
        <div>
          {currentProject.project_images.map(image => <img src={image.url}/>)}
        </div>
      </div>
    </div>
  )
}

export default ProjectDetail;
