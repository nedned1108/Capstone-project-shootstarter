import React from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { thunkDeletePayment } from '../../store/payment_method';
import { thunkLoadAllPayments } from '../../store/payment_method';
import './PaymentMethod.css'


const RemoveCardModal = ({ card }) => {
  const dispatch = useDispatch()
  const {closeModal} = useModal()

  const cancelDelete = () => {
    closeModal()
  }

  const removeCard = (e) => {
    dispatch(thunkDeletePayment(e))
    closeModal()
  }

  return (
    <div className='removeCard'>
      <h3>Confirm Remove Card</h3>
      <div className='removeCardButton'>
        <button onClick={() => removeCard(card.id)} >Remove</button>
        <button onClick={cancelDelete}>Cancel</button>
      </div>
    </div>
  )
}

export default RemoveCardModal;
