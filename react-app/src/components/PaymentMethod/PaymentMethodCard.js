import React from "react";
import { useDispatch, useSelector } from "react-redux";
import RemoveCardModal from "./RemoveCardModal";
import OpenModalButton from '../OpenModalButton'
import EditPaymentMethodModal from "../PaymentMethod/EditPaymentMethodModal";
import './PaymentMethod.css'


const PaymentMethodCard = ({ payment_method }) => {
  
  return (
    <div className="paymentMethodCard">
      <p>{payment_method.name_on_card}</p>
      <div className="cardNum">
        <p>{payment_method.card_type}  ****{payment_method.card_number.slice(9)}</p>
        <p>expires: {payment_method.expire_month}/{payment_method.expire_year}</p>
      </div>
      <div className="cardButton">
        <OpenModalButton 
          buttonText="Update Card"
          modalComponent={<EditPaymentMethodModal card={payment_method}/>}
        />
        <OpenModalButton 
          buttonText="Remove Card"
          modalComponent={<RemoveCardModal card={payment_method}/>}
        />
      </div>
    </div>
  )
}


export default PaymentMethodCard;
