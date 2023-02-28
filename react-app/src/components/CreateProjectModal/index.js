import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkCreateProject } from '../../store/project';
import { useHistory } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import './CreateProjectModal.css'


export default function CreateProjectModal() {
  const dispatch = useDispatch();
  const history = useHistory();
  const [project_name, setProjectName] = useState('');
  const [description, setDescription] = useState('');
  const [story, setStory] = useState('');
  const [risks, setRisks] = useState('');
  const [goal, setGoal] = useState();
  const [end_day, setEndDay] = useState('');
  const [project_type, setProjectType] = useState('');
  const [url, setUrl] = useState('');
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const currentUser = useSelector(state => state.session.user)
  const today = new Date();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);
    if (currentUser == undefined) {
      closeModal()
      return history.push('/login')
    }
    const checkEndDay = new Date(end_day)

    if (checkEndDay <= today) {
      setErrors(['end day can not be today or in the past'])
    } else {
      const project = {
        project_name,
        description,
        story,
        risks,
        goal,
        end_day,
        project_type,
        url
      };
  
      const data = await dispatch(thunkCreateProject(project))
      if (data.errors) {
        setErrors(data.errors)
      } else {
        setErrors([]);
        closeModal()
        history.push(`/project/${data.id}`);
      }
    }
  }

  return (
    <div className='createProjectModal'>
      <h1>
        Create Project
      </h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <div className="input-form">
          <label>Project Name:</label>
          <input
            type='text'
            value={project_name}
            onChange={(e) => setProjectName(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Description:</label>
          <input
            type='text'
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Story:</label>
          <textarea
            type='text'
            value={story}
            onChange={(e) => setStory(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Risks:</label>
          <textarea
            type='text'
            value={risks}
            onChange={(e) => setRisks(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Goal:</label>
          <input
            type='number'
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>End Day:</label>
          <input
            type='date'
            value={end_day}
            onChange={(e) => setEndDay(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Project Type:</label>
          <input
            type='text'
            value={project_type}
            onChange={(e) => setProjectType(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Project Image:</label>
          <input
            type='text'
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
        </div>
        <div>
          <button className='submitButton' type="submit">Create New Project</button>
        </div>
      </form>
    </div>
  )
}
