import React from "react";
import { useDispatch, useSelector } from "react-redux";
import RemoveCardModal from "./RemoveCardModal";
import OpenModalButton from '../OpenModalButton'
import './AddPaymentMethod.css'


const PaymentMethodCard = ({ payment_method }) => {

  return (
    <div className="paymentMethodCard">
      <p>{payment_method.name_on_card}</p>
      <p>****{payment_method.card_number.slice(9)}</p>
      <p>{payment_method.expire_month}/{payment_method.expire_year}</p>
      <p>{payment_method.cvv}</p>
      <p>{payment_method.card_type}</p>
      <button>Edit card</button>
      <OpenModalButton 
        buttonText="Remove Card"
        modalComponent={<RemoveCardModal card={payment_method}/>}
      />
    </div>
  )
}


export default PaymentMethodCard;