import React, { useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from '../OpenModalButton';
import AddPaymentMethod from '../PaymentMethod/AddPaymentMethod';
import PaymentMethodModal from "../PaymentMethod/PaymentMethodModal"
import './PledgeCard.css'

const PaymentModal = ({ payment_methods, choice }) => {
  const dispatch = useDispatch();

  return (
    <div className='paymentMethodModal'>
      <div>
        <h1>Payment Methods</h1>
        <OpenModalButton 
          buttonText='Add your card'
          modalComponent={<AddPaymentMethod />}
        />
        {payment_methods != 0 ? payment_methods.map(payment_method => <PaymentMethodModal payment_method={payment_method} choice={choice}/>) : <h4>No payment method</h4>}
      </div>
    </div>
  )
}

export default PaymentModal;
