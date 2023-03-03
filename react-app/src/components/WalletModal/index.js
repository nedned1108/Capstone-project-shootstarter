import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkLoadAllPayments } from '../../store/payment_method';
import './WalletModal.css'

const WalletModal = () => {
  const dispatch = useDispatch();
  const payment_methodsData = useSelector(state => state.payment.payments)
  let payment_methods;
  if (payment_methodsData) {
    payment_methods = Object.values(payment_methodsData)
  }

  useEffect(() => {
    dispatch(thunkLoadAllPayments())
  }, [dispatch])

  if (!payment_methodsData) {
    return null
  }

  return (
    <h1>Payment Methods</h1>
  )
}

export default WalletModal;
