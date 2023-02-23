import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkCreatePledge } from '../../store/pledge';
import { useParams } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import './CreatePledgeModal.css'


const CreatePledgeModal = ({ projectId }) => {
  const dispatch = useDispatch();
  const currentUser = useSelector(state => state.session.user)
  const { closeModal } = useModal();
  const [pledge_name, setPledgeName] = useState('');
  const [price, setPrice] = useState();
  const [ships_to, setShipTo] = useState('');
  const [rewards, setRewards] = useState('');
  const [estimated_delivery, setEstimatedDelivery] = useState();
  const [errors, setErrors] = useState([]);
  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const pledge = {
      pledge_name,
      price,
      ships_to,
      rewards,
      estimated_delivery,
      project_id: projectId
    }
    const data = await dispatch(thunkCreatePledge(pledge))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      closeModal()
    }
  }

  return (
    <div className='mainDiv'>
      <div className='createPledge'>
        <h1>
          Create Pledge
        </h1>
        <form onSubmit={handleSubmit}>
          <ul>
            {errors.map((error, idx) => <li key={idx}>{error}</li>)}
          </ul>
          <div className="input-form">
            <label>Pledge Name:</label>
            <input
              type='text'
              value={pledge_name}
              onChange={(e) => setPledgeName(e.target.value)}
              required
            />
          </div>
          <div className="input-form">
            <label>Price:</label>
            <input
              type='number'
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Ship To:</label>
            <textarea
              type='text'
              value={ships_to}
              onChange={(e) => setShipTo(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Rewards:</label>
            <textarea
              type='text'
              value={rewards}
              onChange={(e) => setRewards(e.target.value)}
              required
            />
          </div>
          <div className="input-form">
            <label>Estimated Delivery:</label>
            <input
              type='text'
              value={estimated_delivery}
              onChange={(e) => setEstimatedDelivery(e.target.value)}
              required
            />
          </div>
          <div>
            <button className='submit-button' type="submit">Create New Pledge</button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CreatePledgeModal;
