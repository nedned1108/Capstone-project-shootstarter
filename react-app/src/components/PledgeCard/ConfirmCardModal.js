import React from 'react';
import { useModal } from "../../context/Modal"
import { thunkChoosePledge } from '../../store/pledge';
import PaymentModal from './PaymentModal';
import { useDispatch } from 'react-redux';

import './PledgeCard.css'

const ConfirmCardModal = ({ payment_method, choice }) => {
  const dispatch = useDispatch()
  const {closeModal} = useModal()

  const cancel = () => {
    closeModal()
  }
  const confirm = () => {
    dispatch(thunkChoosePledge(choice))
    closeModal()
  }
  return (
    <div className='confirmPaymentModal'>
      <h3>Confirm Payment</h3>
      <div className='confirmPaymentButton'>
        <button onClick={confirm} >Confirm</button>
        <button onClick={cancel} >Cancel</button>
      </div>
    </div>
  )
}

export default ConfirmCardModal;
