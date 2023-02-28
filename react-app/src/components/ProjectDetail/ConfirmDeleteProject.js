import React from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { thunkDeleteProject } from '../../store/project';
import './ProjectDetail.css'


const ConfirmDeleteProject = ({ project }) => {
  const { closeModal } = useModal()
  const dispatch = useDispatch()
  const history = useHistory()

  const cancelDelete = () => {
    closeModal()
  }
  const deleteProject = (e) => {
    dispatch(thunkDeleteProject(e))
    history.push('/')
  }

  return (
    <div className='deleteProject'>
      <h3>Confirm Delete Project</h3>
      <div className='deleteProjectButton'>
        <button onClick={() => deleteProject(project.id)} >Delete</button>
        <button onClick={cancelDelete} >Cancel</button>
      </div>
    </div>
  )
}

export default ConfirmDeleteProject;
