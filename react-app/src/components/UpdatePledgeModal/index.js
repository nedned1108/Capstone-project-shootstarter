import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkUpdatePledge } from '../../store/pledge';
import { useParams } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import './UpdatePledgeModal.css'


const UpdatePledgeModal = ({ pledge }) => {
  const dispatch = useDispatch();
  const currentUser = useSelector(state => state.session.user)
  const { closeModal } = useModal();
  const [pledge_name, setPledgeName] = useState(pledge.pledge_name);
  const [price, setPrice] = useState(pledge.price);
  const [ships_to, setShipTo] = useState(pledge.ships_to);
  const [rewards, setRewards] = useState(pledge.rewards);
  const [estimated_delivery, setEstimatedDelivery] = useState(pledge.estimated_delivery);
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const pledgeData = {
      ...pledge,
      pledge_name,
      price,
      ships_to,
      rewards,
      estimated_delivery
    }
    const data = await dispatch(thunkUpdatePledge(pledgeData))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      closeModal()
    }
  }

  return (
    <div className='updatePledgeModal'>
      <h1>
        Update Pledge
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
        <div className="input-form">
          <label>Ship To:</label>
          <input
            type='text'
            value={ships_to}
            onChange={(e) => setShipTo(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
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
          <button className='submitButton' type="submit">Update Pledge</button>
        </div>
      </form>
    </div>
  )
}


export default UpdatePledgeModal;
