import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkCreateComment } from '../../store/comment';
import { useParams } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import './CreateCommentModal.css'


const CreateCommentModal = ({ project_id }) => {
  const dispatch = useDispatch();
  const currentUser = useSelector(state => state.session.user)
  const { closeModal } = useModal();
  const [comment, setComment] = useState('')
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const commentData = {
      comment,
      project_id
    }
    const data = await dispatch(thunkCreateComment(commentData))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      closeModal()
    }
  }

  return (
    <div className='createCommentModal'>
      <h1>
        Comment
      </h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <div className="input-form">
          <label>Your Comment:</label>
          <textarea
            type='text'
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            required
          />
          <div>
            <button className='submitButton' type="submit">Submit Comment</button>
          </div>
        </div>
      </form>
    </div>
  )
}

export default CreateCommentModal;
