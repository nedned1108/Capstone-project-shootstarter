import React, { useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkUpdateProject } from "../../store/project";
import './UpdateProjectModal.css'

const UpdateProjectModal = ({ project }) => {
  const dispatch = useDispatch();
  const currentUser = useSelector(state => state.session.user)
  const [project_name, setProjectName] = useState(project.project_name);
  const [description, setDescription] = useState(project.description);
  const [story, setStory] = useState(project.story);
  const [risks, setRisks] = useState(project.risks);
  const [goal, setGoal] = useState(project.goal);
  const [end_day, setEndDay] = useState(project.end_day);
  const [project_type, setProjectType] = useState(project.project_type);
  const [url, setUrl] = useState(project.project_images[0].url);
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const today = new Date();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);
    const checkEndDay = new Date(end_day)

    if (checkEndDay <= today) {
      setErrors(['end day can not be today or in the past'])
    } else {
      const projectData = {
        ...project,
        project_name,
        description,
        story,
        risks,
        goal,
        end_day,
        project_type,
        url
      };

      const data = await dispatch(thunkUpdateProject(projectData))
      if (data.errors) {
        setErrors(data.errors)
      } else {
        setErrors([]);
        closeModal();
      }
    }
  }

  return (
    <div className='updateProjectModal'>
      <h1>
        Update Project
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
        <div>
          <button className='submitButton' type="submit">Update Project</button>
        </div>
      </form>
    </div>
  )
}

export default UpdateProjectModal;
