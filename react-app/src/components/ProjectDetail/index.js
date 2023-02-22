import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useParams } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { thunkLoadAllProjects } from "../../store/project";
import { thunkDeleteProject } from "../../store/project";
import UpdateProjectModal from "../UpdateProjectModal";
import OpenModalButton from "../OpenModalButton";


const ProjectDetail = () => {
  const { projectId } = useParams();
  const dispatch = useDispatch();
  const projects = useSelector(state => state.project.projects)
  const currentProject = Object.values(projects).find(project => project.id == projectId)
  const currentUser = useSelector(state => state.session.user)

  useEffect(() => {
    dispatch(thunkLoadAllProjects())
  }, [dispatch, projectId])

  if (!currentProject) {
    return null
  }

  return (
    <div>
      <div>
        <h2>{currentProject.project_name}</h2>
        <h3>{currentProject.description}</h3>
      </div>
      <div>
        <div>
          <img src={currentProject.project_images[0].url}/>
        </div>
        <div>
          <div>
            <h4>${currentProject.current_fund}</h4>
            <p>pledged of ${currentProject.goal}</p>
            <h4>{currentProject.backers}</h4>
            <p>backers</p>
            <h4>{currentProject.end_day}</h4>
            {currentUser && currentUser.id == currentProject.user_id ?
            <>
              <OpenModalButton 
                buttonText="Update Project"
                modalComponent={<UpdateProjectModal project={currentProject}/>}
              />
              <button>Delete</button>
            </>
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
