import React from 'react';
import { useModal } from "../../context/Modal"
import { thunkChoosePledge } from '../../store/pledge';
import PaymentModal from './PaymentModal';
import { useDispatch } from 'react-redux';
import { authenticate } from "../../store/session";

import './PledgeCard.css'

const ConfirmCardModal = ({ payment_method, choice }) => {
  const dispatch = useDispatch()
  const {closeModal} = useModal()

  const cancel = () => {
    closeModal()
  }
  const confirm = async () => {
    await dispatch(thunkChoosePledge(choice))
    dispatch(authenticate())
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
