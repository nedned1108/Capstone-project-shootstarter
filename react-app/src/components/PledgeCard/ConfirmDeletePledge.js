import React, { useEffect, useState } from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { thunkDeletePledge } from '../../store/pledge';
import './PledgeCard.css'

const ConfirmDeletePledge = ({ pledge }) => {
  const { closeModal } = useModal()
  const dispatch = useDispatch()

  const cancelDelete = () => {
    closeModal()
  }
  const deletePledge = (e) => {
    dispatch(thunkDeletePledge(e))
    closeModal()
  }
  return (
    <div>
      <h1>Confirm Delete</h1>
      <button onClick={() => deletePledge(pledge.id)} >Delete</button>
      <button onClick={cancelDelete} >Cancel</button>
    </div>
  )
}

export default ConfirmDeletePledge;
