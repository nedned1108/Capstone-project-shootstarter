import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import OpenModalButton from '../OpenModalButton'
import ConfirmCardModal from '../PledgeCard/ConfirmCardModal';
import './AddPaymentMethod.css'


const PaymentMethodModal = ({ payment_method, choice }) => {

  return (
    <div className="paymentMethod">
      <p>{payment_method.name_on_card}</p>
      <p>****{payment_method.card_number.slice(9)}</p>
      <p>{payment_method.expire_month}/{payment_method.expire_year}</p>
      <p>{payment_method.cvv}</p>
      <p>{payment_method.card_type}</p>
      <OpenModalButton 
        buttonText="Use This Card"
        modalComponent={<ConfirmCardModal card={payment_method} choice={choice}/>}
      />
    </div>
  )
}

export default PaymentMethodModal;
