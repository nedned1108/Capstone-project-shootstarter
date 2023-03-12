import React, { useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";
import PaymentMethodModal from "../PaymentMethod/PaymentMethodModal"
import './PledgeCard.css'

const PaymentModal = ({ payment_methods, choice }) => {
  const dispatch = useDispatch();

  return (
    <div className='paymentMethodModal'>
        {payment_methods.length == 0 ? "No payment method" : 
          <div>
            <h1>Choose your payment methods</h1>
            {payment_methods.map(payment_method => <PaymentMethodModal payment_method={payment_method} choice={choice}/>)}
          </div>
        }
    </div>
  )
}

export default PaymentModal;
