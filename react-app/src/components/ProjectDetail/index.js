import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { thunkLoadAllProjects } from "../../store/project";
import { thunkLoadAllComments } from "../../store/comment";
import UpdateProjectModal from "../UpdateProjectModal";
import OpenModalButton from "../OpenModalButton";
import AddImageModal from "./AddImageModal";
import ConfirmDeleteProject from "./ConfirmDeleteProject";
import CommentCard from "../CommentCard";
import CreateCommentModal from "../CreateCommentModal";

import './ProjectDetail.css'
import no_image from '../../images/empty-image.png' 
import user_image from '../../images/default-user.png'

const ProjectDetail = () => {
  const { projectId } = useParams();
  const dispatch = useDispatch();
  const projects = useSelector(state => state.project.projects)
  const comments = useSelector(state => state.comment.comments)
  const currentProject = Object.values(projects).find(project => project.id == projectId)
  const currentUser = useSelector(state => state.session.user)
  let projectComments;
  if (comments) {
    projectComments = Object.values(comments).filter(comment => comment.project_id == projectId)
  }
  let daysToGo
  let today = new Date()
  if (currentProject) {
    const oneDay = 1000*60*60*24;
    const endDay = new Date(currentProject.end_day.split('-').join('/'))
    daysToGo = Math.ceil((endDay.getTime() - today.getTime())/oneDay)
  }
  useEffect(() => {
    dispatch(thunkLoadAllProjects())
    dispatch(thunkLoadAllComments())
  }, [dispatch, projectId])

  const func = (e) => {
    const el = document.getElementsByClassName(e)
    el[0].scrollIntoView()
  }

  const onImageError = (e) => {
    e.target.src = no_image
  }
  const onProfileImageError = (e) => {
    e.target.src = user_image
  }

  if (!currentProject) {
    return null
  }

  return (
    <div className="projectMainDiv">
      <div className="projectTitle">
        <h2>{currentProject.project_name}</h2>
        <h3>{currentProject.description}</h3>
      </div>
      <div className="projectImgInfo">
        <div className="projectImg">
          <img src={currentProject.project_images[0].url} onError={onImageError}/>
        </div>
        <div className="projectInfo">
          <div className="projectInfoNum">
            <h4 className="currentFund">${currentProject.current_fund}</h4>
            <p>pledged of ${currentProject.goal}</p>
            <h4>{currentProject.backers}</h4>
            <p>backers</p>
            <h4>{daysToGo}</h4>
            <p>days to go</p>
            <div className="pledgeButton">
              <NavLink to={`/project/${currentProject.id}/pledge`}>
                Back this project
              </NavLink>
            </div>
            {currentUser && currentUser.id == currentProject.owner_id ? 
            <div className="editDelete">
              <OpenModalButton 
                buttonText="Update Project"
                modalComponent={<UpdateProjectModal project={currentProject}/>}
              />
              <OpenModalButton 
                buttonText="Delete Project"
                modalComponent={<ConfirmDeleteProject project={currentProject}/>}
              />
              <OpenModalButton 
                buttonText="Add Images"
                modalComponent={<AddImageModal project_id={currentProject.id}/>}
              />
            </div>
            : '' 
            } 
          </div>
        </div>
      </div>
      <div className="bottomMainDiv">
        <div>
          <div className="leftDiv">
            <button className="storyButton" onClick={() => func("story")}>STORY</button>
            <button className="riskButton" onClick={() => func("risks")}>RISKS</button>
            <button className="commentButton" onClick={() => func("comments")}>COMMENTS</button>
          </div>
        </div>
        <div className="middleDiv">
          <div>
            <h2 className="story">Story</h2>
            {currentProject.story}
          </div>
          <div className="middleDivImg">
            {currentProject.project_images.map(image => <img src={image.url} onError={onImageError}/>)}
          </div>
          <div>
            <h2>Terms and Condition</h2>
            By pledging to this project, you acknowledge that the final look, materials, and content of the rewards (and the project) are subject to change and may differ substantially from what is presented in this Kickstarter project.  
            If you do not log in and confirm your pledge within 8 weeks of our notification via email to confirm your pledge, you agree that we have fulfilled our obligations to you in full for payment or donations received. 
            However, we may, at our discretion, refund or ship your pledge if you contact us and confirm your pledge after the 8 week window has elapsed.  If you confirm your pledge within 8 weeks of our notification via email, 
            you agree that our responsibility to you is to ship your order as entered into our pledge manager system, that title and risk passes to you upon delivery to a common carrier for such shipment, and you are responsible for import 
            duties or any other duties that may be payable to the relevant tax authorities, providing correct address information and ensuring this address is deliverable by normal methods. We regret we are unable to ship to PO Boxes.  
            If these terms are not acceptable to you, then we suggest that you do not participate in this crowdfunding campaign and acquire the game when it is released in stores. Thank you for your understanding.
          </div>
          <div>
            <h2 className="risks">Risks</h2>
            {currentProject.risks}
          </div>
          <div className="comments">
            <h2>Comments</h2>
            {currentUser && currentUser.id != currentProject.owner_id &&
              <OpenModalButton 
                buttonText="Add your comment"
                modalComponent={<CreateCommentModal project_id={currentProject.id} />}
              />
            }
            <div className="commentMainDiv">
              {projectComments && projectComments.map(comment => <CommentCard comment={comment}/>)}
            </div>
          </div>
        </div>
        <div>
          <div className="rightDiv">
            <img alt="owner-profile-image" src={currentProject.owner.profile_image} onError={onProfileImageError}/>
            <h4>{currentProject.owner.first_name} {currentProject.owner.last_name}</h4>
            <p>{currentProject.owner.bio}</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProjectDetail;
