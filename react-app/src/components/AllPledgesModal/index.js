import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkLoadAllPledges } from '../../store/pledge';
import './AllPledgesModal.css'

const AllPledgesModal = () => {
  const dispatch = useDispatch();
  const allPledgesData = useSelector(state => state.pledge.pledges)
  const currentUser = useSelector(state => state.session.user)
  
  useEffect(() => {
    dispatch(thunkLoadAllPledges())
  }, [dispatch])

  let pledges = [];
  if (allPledgesData) {
    for (let num of currentUser.pledges) {
      pledges.push(Object.values(allPledgesData).find(pledge => pledge.id == num))
    }
  }

  return (
    <div className='yourPledgeDiv'>
      <h1>Your Pledges</h1>
      <div>
        {pledges.length != 0 ? 
          pledges.map(pledge => <div>{pledge.pledge_name}</div>)
          : "You have no pledge"
        }
      </div>
    </div>
  )
}

export default AllPledgesModal;
