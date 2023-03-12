import React, { useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";
import './PledgeCard.css'

const PaymentModal = () => {
  const dispatch = useDispatch();

  return (
    <div className='thankyouDiv'>
        <h1>Thank you for choosing your reward</h1>
    </div>
  )
}

export default PaymentModal;
