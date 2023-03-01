import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkUpdateComment } from '../../store/comment';
import { useModal } from '../../context/Modal';
import './UpdateCommentModal.css'


const UpdateCommentModal = ({ commentDetail }) => {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const [comment, setComment] = useState(commentDetail.comment)
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const commentData = {
      ...commentDetail,
      comment
    }
    const data = await dispatch(thunkUpdateComment(commentData))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      closeModal()
    }
  }

  return (
    <div className='updateCommentModal'>
      <h1>
        Update Your Comment
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
          <button className='submitButton' type="submit">Update Comment</button>
        </div>
      </div>
      </form>
    </div>
  )
}

export default UpdateCommentModal;
