import React from "react";
import { useDispatch, useSelector } from "react-redux";
import UpdateCommentModal from "../UpdateCommentModal";
import OpenModalButton from "../OpenModalButton";
import ConfirmDeleteComment from "./ConfirmDeleteComment";
import './CommentCard.css'
import user_image from '../../images/default-user.png'

const CommentCard = ({ comment }) => {
  const currentUser = useSelector(state => state.session.user)
  const createDate = new Date(comment.created_at.split('-').join('/')).toDateString().split(' ').splice(1).join(' ')
  const onProfileImageError = (e) => {
    e.target.src = user_image
  }

  return (
    <div className="singleCommentDiv">
      <div className="userInfo">
        <div className="userInfoImgDiv">
          <img alt="profile-image" className="userImage" src={comment.user.profile_image} onError={onProfileImageError}/>
          <div className="username_time">
            <p style={{fontWeight: "600"}}>{comment.user.username}</p>
            <p>{createDate}</p>
          </div>
        </div>
        {
          currentUser && comment.user_id == currentUser.id ?
            <div className="editDeleteComment">
              <OpenModalButton 
                buttonText={<i class="fa-solid fa-pen-to-square"></i>}
                modalComponent={<UpdateCommentModal commentDetail={comment}/>}
              />
              <OpenModalButton 
                buttonText={<i class="fa-solid fa-trash"></i>}
                modalComponent={<ConfirmDeleteComment commentDetail={comment}/>}
              />
            </div>
          : ''
        }
      </div>
      <div>
        <p>{comment.comment}</p>
      </div>
    </div>
  )
}

export default CommentCard;
