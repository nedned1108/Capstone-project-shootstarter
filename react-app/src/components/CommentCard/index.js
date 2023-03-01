import React from "react";
import { useDispatch, useSelector } from "react-redux";
import './CommentCard.css'

const CommentCard = ({ comment }) => {
  const currentUser = useSelector(state => state.session.user)

  return (
    <div className="singleCommentDiv">
      <div className="userInfo">
        <div className="userInfoImgDiv">
          <img className="userImage" src={comment.user.profile_image}/>
          {comment.user.username}
        </div>
        {
          currentUser && comment.user_id == currentUser.id ?
            <div>
              <button>{<i class="fa-solid fa-pen-to-square"></i>}</button>
              <button>{<i class="fa-solid fa-trash"></i>}</button>
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
