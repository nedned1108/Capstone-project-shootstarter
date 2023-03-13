import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import OpenModalButton from '../OpenModalButton'
import ConfirmCardModal from '../PledgeCard/ConfirmCardModal';
import './PaymentMethod.css'
import mastercard from "../../images/Mastercard.png"
import visa from "../../images/Visa.png"
import discover from "../../images/Discover.png"
import american_express from "../../images/American-Express.png"


const PaymentMethodModal = ({ payment_method, choice }) => {

  return (
    <div className="paymentMethod">
      <div className="cardNameType">
        <p>Card Holder: {payment_method.name_on_card}</p>
        {payment_method.card_type == "Mastercard" ? <img className="cardTypeImg" src={mastercard}/> : ""}
        {payment_method.card_type == "Discover" ? <img className="cardTypeImg" src={discover}/> : ""}
        {payment_method.card_type == "Visa" ? <img className="cardTypeImg" src={visa}/> : ""}
        {payment_method.card_type == "American Express" ? <img className="cardTypeImg" src={american_express}/> : ""}
      </div>
      <div className="cardNum">
        <p>{payment_method.card_type}  ****{payment_method.card_number.slice(8)}</p>
        <p>expires: {payment_method.expire_month}/{payment_method.expire_year}</p>
      </div>
      <OpenModalButton 
        buttonText="Use This Card"
        modalComponent={<ConfirmCardModal card={payment_method} choice={choice}/>}
      />
    </div>
  )
}

export default PaymentMethodModal;
