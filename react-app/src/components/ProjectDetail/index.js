import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Link, useParams } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { thunkLoadAllProjects } from "../../store/project";


const ProjectDetail = () => {
  const { projectId } = useParams();
  const dispatch = useDispatch();
  const projects = useSelector(state => state.project.projects)
  const currentProject = Object.values(projects).find(project => project.id == projectId)
  console.log(currentProject)

  useEffect(() => {
    dispatch(thunkLoadAllProjects())
  }, [dispatch, projectId])

  return (
    <h1>Project Detail</h1>
  )
}

export default ProjectDetail;
