import React, {useEffect, useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkCreatePayment } from "../../store/payment_method";
import WalletModal from ".";
import './WalletModal.css'


const AddPaymentMethod = () => {
  const dispatch = useDispatch();
  const [name_on_card, setNameOnCard] = useState('')
  const [card_number, setCardNumber] = useState('')
  const [expire_month, setExpireMonth] = useState(1)
  const [expire_year, setExpireYear] = useState()
  const [cvv, setCvv] = useState()
  const [card_type, setCardType] = useState('Mastercard')
  const [add_payment, setAddPayment] = useState(true)
  const [errors, setErrors] = useState([]);
  const { setModalContent } = useModal()

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const cardData = {
      name_on_card,
      card_number,
      expire_month,
      expire_year,
      cvv,
      card_type
    }
    const data = await dispatch(thunkCreatePayment(cardData))
    if (data.errors) {
      setErrors(data.errors)
    } else {
      setErrors([]);
      setModalContent(<WalletModal />)
    }
  }

  return (
    <div>
      <h1>
        Add your card
      </h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <div className="input-form">
          <label>Name on Card:</label>
          <input
            type='text'
            value={name_on_card}
            onChange={(e) => setNameOnCard(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Card Number:</label>
          <input
            type='number'
            value={card_number}
            onChange={(e) => setCardNumber(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
          <label>Expire:</label>
          <select
            type='number'
            value={expire_month}
            onChange={(e) => setExpireMonth(e.target.value)}
            required
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
          />
        </div>
        <div className="input-form">
          <label>CVV:</label>
          <input
            type='number'
            value={cvv}
            onChange={(e) => setCvv(e.target.value)}
            required
          />
        </div>
        <div className="input-form">
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
          <button className='submitButton' type="submit">Add Card</button>
        </div>
      </form>
    </div>
  )
}

export default AddPaymentMethod;
