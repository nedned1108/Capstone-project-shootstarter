import React from "react";
import { useDispatch, useSelector } from "react-redux";
import UpdateCommentModal from "../UpdateCommentModal";
import OpenModalButton from "../OpenModalButton";
import ConfirmDeleteComment from "./ConfirmDeleteComment";
import './CommentCard.css'

const CommentCard = ({ comment }) => {
  const currentUser = useSelector(state => state.session.user)
  const createDate = new Date(comment.created_at)

  return (
    <div className="singleCommentDiv">
      <div className="userInfo">
        <div className="userInfoImgDiv">
          <img className="userImage" src={comment.user.profile_image}/>
          <div className="username_time">
            <p style={{fontWeight: "600"}}>{comment.user.username}</p>
            <p>{createDate.toDateString()}</p>
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
