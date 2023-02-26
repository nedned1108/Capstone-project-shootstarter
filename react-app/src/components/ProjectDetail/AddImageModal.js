import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import { thunkAddImages } from '../../store/project';
import { thunkLoadAllProjects } from '../../store/project';


const AddImageModal = ({ project_id }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { closeModal } = useModal();
  const [url, setUrl] = useState('');
  const [errors, setErrors] = useState([]);
  const currentUser = useSelector(state => state.session.user)

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);
    if (currentUser == undefined) {
      closeModal()
      return history.push('/login')
    }
    const image = {
      url,
      project_id
    };

    const data = await dispatch(thunkAddImages(image))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      closeModal()
      dispatch(thunkLoadAllProjects())
    }
  }
  return (
    <div>
      <h1>Add Images</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <div className="input-form">
          <label>Image Url:</label>
          <input
            type='text'
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
        </div>
        <div>
          <button className='submitButton' type="submit">Add New Project Image</button>
        </div>
      </form>
    </div>
  )
}

export default AddImageModal;
