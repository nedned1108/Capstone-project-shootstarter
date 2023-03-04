import React from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch } from 'react-redux';
import { thunkDeletePayment } from '../../store/payment_method';
// import { Modal } from '../../context/Modal';
import WalletModal from '.';
import './WalletModal.css'


const RemoveCardModal = ({ card }) => {
  const dispatch = useDispatch()
  const {setModalContent} = useModal()

  const cancelDelete = () => {
    setModalContent(<WalletModal/>)
  }

  const removeCard = (e) => {
    dispatch(thunkDeletePayment(e))
    setModalContent(<WalletModal />)
  }

  return (
    <div className='removeCard'>
      <h3>Confirm Remove Card</h3>
      <div className='removeCardButton'>
        <button onClick={() => removeCard(card.id)} >Remove</button>
        <button onClick={cancelDelete}>Cancel</button>
      </div>
    </div>
  )
}

export default RemoveCardModal;
