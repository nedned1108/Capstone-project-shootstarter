import React from "react";
import { useDispatch, useSelector } from "react-redux";
import RemoveCardModal from "./RemoveCardModal";
import OpenModalButton from '../OpenModalButton'
import EditPaymentMethodModal from "../PaymentMethod/EditPaymentMethodModal";
import './PaymentMethod.css'
import mastercard from "../../images/Mastercard.png"
import visa from "../../images/Visa.png"
import discover from "../../images/Discover.png"
import american_express from "../../images/American-Express.png"


const PaymentMethodCard = ({ payment_method }) => {

  return (
    <div className="paymentMethodCard">
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
