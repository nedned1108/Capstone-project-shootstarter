import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkUpdatePayment } from "../../store/payment_method";
import './AddPaymentMethod.css' 


const EditPaymentMethodModal = () => {
  const dispatch = useDispatch()

}

export default EditPaymentMethodModal;
