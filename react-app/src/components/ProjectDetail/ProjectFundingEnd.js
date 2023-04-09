import React from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import './ProjectDetail.css'

const ProjectFundingEnd = () => {

  return (
    <div>
      <h3>Project Funding Ended</h3>
      <p>Please choose another project</p>
    </div>
  )
}

export default ProjectFundingEnd;
