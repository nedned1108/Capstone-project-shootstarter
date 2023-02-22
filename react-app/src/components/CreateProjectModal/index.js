import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkCreateProject } from '../../store/project';
import { useHistory } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import './CreateProjectModal.css'


export default function CreateProjectModal() {
  const dispatch = useDispatch();
  const { user } = useSelector(state => state.session)
  const history = useHistory();
  const [projectName, setProjectName] = useState('');
  const [description, setDescription] = useState('');
  const [story, setStory] = useState('');
  const [risks, setRisks] = useState('');
  const [goal, setGoal] = useState();
  const [endDay, setEndDay] = useState('');
  const [projectType, setProjectType] = useState('');
  const [url, setUrl] = useState('');
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const currentUser = useSelector(state => state.session.user)

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);
    if (currentUser == undefined) return history.push('/login')

    const project = {
      projectName,
      description,
      story,
      risks,
      goal,
      endDay,
      projectType,
      url,
    };

    const data = await dispatch(thunkCreateProject(project))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      history.push(`/project/${data.id}`);
    }
  }

  return (
    <div className='mainDiv'>
      <div className='createProject'>
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
              value={projectName}
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
          <div>
            <label>Story:</label>
            <textarea
              type='text'
              value={story}
              onChange={(e) => setStory(e.target.value)}
              required
            />
          </div>
          <div>
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
              type='text'
              value={goal}
              onChange={(e) => setGoal(e.target.value)}
              required
            />
          </div>
          <div className="input-form">
            <label>End Day:</label>
            <input
              type='text'
              value={endDay}
              onChange={(e) => setEndDay(e.target.value)}
              required
            />
          </div>
          <div className="input-form">
            <label>Project Type:</label>
            <input
              type='text'
              value={projectType}
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
            <button className='submit-button' type="submit">Create New Project</button>
          </div>
        </form>
      </div>
    </div>
  )
}
