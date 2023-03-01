import React from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { thunkDeleteComment } from '../../store/comment';
import './CommentCard.css'

const ConfirmDeleteComment = ({ commentDetail }) => {
  const { closeModal } = useModal()
  const dispatch = useDispatch()

  const cancelDelete = () => {
    closeModal()
  }
  const deleteComment= (e) => {
    dispatch(thunkDeleteComment(e))
    closeModal()
  }

  return (
    <div className='deleteComment'>
      <h3>Confirm Delete Comment</h3>
      <div className='deleteCommentButton'>
        <button onClick={() => deleteComment(commentDetail.id)} >Delete</button>
        <button onClick={cancelDelete} >Cancel</button>
      </div>
    </div>
  )
}

export default ConfirmDeleteComment;
