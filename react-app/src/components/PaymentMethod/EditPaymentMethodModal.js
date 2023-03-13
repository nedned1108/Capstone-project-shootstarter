import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkUpdatePayment } from "../../store/payment_method";
import './PaymentMethod.css' 


const EditPaymentMethodModal = ({ card }) => {
  const dispatch = useDispatch()
  const [name_on_card, setNameOnCard] = useState(card.name_on_card)
  const [card_number, setCardNumber] = useState(card.card_number)
  const [expire_month, setExpireMonth] = useState(card.expire_month)
  const [expire_year, setExpireYear] = useState(card.expire_year)
  const [cvv, setCvv] = useState(card.cvv)
  const [card_type, setCardType] = useState(card.card_type)
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const cardData = {
      ...card,
      name_on_card,
      card_number,
      expire_month,
      expire_year,
      cvv,
      card_type
    }
    const data = await dispatch(thunkUpdatePayment(cardData))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      closeModal()
    }
  }

  return (
    <div className="addPaymentMethod">
      <h1>
        Update your card
      </h1>
      <form className="addPaymentForm" onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <div className="credit-form">
          <label>Name on Card:</label>
          <input
            type='text'
            value={name_on_card}
            onChange={(e) => setNameOnCard(e.target.value)}
            required
          />
        </div>
        <div className="credit-form">
          <label>Card Number:</label>
          <input
            type='number'
            value={card_number}
            onChange={(e) => setCardNumber(e.target.value)}
            required
          />
        </div>
        <div className="expire">
          <label>Expire:</label>
          <div>
            <select
              type='number'
              value={expire_month}
              onChange={(e) => setExpireMonth(e.target.value)}
              required
              className="expire_month"
            >
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
              <option>6</option>
              <option>7</option>
              <option>8</option>
              <option>9</option>
              <option>10</option>
              <option>11</option>
              <option>12</option>
            </select>
            <input
              type='number'
              value={expire_year}
              onChange={(e) => setExpireYear(e.target.value)}
              required
              className="expire_year"
            />
          </div>
        </div>
        <div className="credit-form">
          <label>CVV:</label>
          <input
            type='number'
            value={cvv}
            onChange={(e) => setCvv(e.target.value)}
            required
          />
        </div>
        <div className="credit-form">
          <label>Card Type:</label>
          <select
            type='text'
            value={card_type}
            onChange={(e) => setCardType(e.target.value)}
            required
          >
            <option>Mastercard</option>
            <option>Visa</option>
            <option>American Express</option>
            <option>Discovery</option>
          </select>
        </div>
        <div>
          <button className='submitButton' type="submit">Update Card</button>
        </div>
      </form>
    </div>
  )
}

export default EditPaymentMethodModal;
