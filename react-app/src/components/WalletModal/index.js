import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkLoadAllPayments } from '../../store/payment_method';
import { useModal } from '../../context/Modal';
import PaymentMethodCard from './PaymentMethodCard';
import AddPaymentMethod from './AddPaymentMethod';
import './WalletModal.css'

const WalletModal = () => {
  const dispatch = useDispatch();
  const { setModalContent } = useModal()
  const payment_methodsData = useSelector(state => state.payment.payments)

  let payment_methods;
  if (payment_methodsData) {
    payment_methods = Object.values(payment_methodsData)
  }

  useEffect(() => {
    dispatch(thunkLoadAllPayments())
  }, [dispatch])

  const addCard = () => {
    setModalContent(<AddPaymentMethod />)
  }

  if (!payment_methodsData) {
    return null
  }

  return (
    <div className='WalletMainDiv'>
      <h1>Payment Methods</h1>
      <button onClick={addCard}>Add your card</button> :
      {payment_methods && payment_methods.map(payment_method => <PaymentMethodCard payment_method={payment_method}/>)}
    </div>
  )
}

export default WalletModal;
