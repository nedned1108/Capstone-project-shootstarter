import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { thunkLoadAllProjects } from "../../store/project";
import { thunkLoadAllPayments } from "../../store/payment_method";
import { thunkLoadAllPledges } from "../../store/pledge";
import PaymentMethodCard from "../WalletModal/PaymentMethodCard";
import './UserProfilePage.css'


const UserProfilePage = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const [yourPledges, setYourPledges] = useState(true)
  const [wallet, setWallet] = useState(false)
  const currentUser = useSelector(state => state.session.user)
  const allPledgesData = useSelector(state => state.pledge.pledges)
  const payment_methodsData = useSelector(state => state.payment.payments)
  let payment_methods;
  if (payment_methodsData) {
    payment_methods = Object.values(payment_methodsData)
  }
  let pledges = [];
  if (allPledgesData) {
    for (let num of currentUser.pledges) {
      pledges.push(Object.values(allPledgesData).find(pledge => pledge.id == num))
    }
  }

  useEffect(() => {
    dispatch(thunkLoadAllProjects())
    dispatch(thunkLoadAllPayments())
    dispatch(thunkLoadAllPledges())
  }, [dispatch])

  const pledgesButton = () => {
    setYourPledges(true)
    setWallet(false)
  }
  const walletButton = () => {
    setYourPledges(false)
    setWallet(true)
  }
  if (!currentUser) {
    return (history.push('/'))
  }
  if (!allPledgesData) {
    return null
  }
  console.log(allPledgesData)
  console.log(pledges)
  return (
    <div className="profileMainDiv">
      <h1>User Profile</h1>
      <div>
        {currentUser && 
          <div>
            <div>
              <img className="userProfile" src={currentUser.profile_image}/>
            </div>
            <div>
              <p>{currentUser.username}</p>
              <p>{currentUser.first_name} {currentUser.last_name}</p>
              <p>{currentUser.bio}</p>
            </div>
            <button onClick={pledgesButton}>Pledges</button>  
            <button onClick={walletButton}>Wallet</button>  
          </div>
        }
        {yourPledges == true ?
          <div>
            <h3>Your Pledges</h3>
            <div>
              {/* {pledges.length != 0 ? 
                pledges.map(pledge => <div>{pledge.pledge_name}</div>)
                : "You have no pledge"
              } */}
            </div>
          </div>
          :
          <div>
            <h3>Wallet</h3>
            <div>
            {payment_methods && payment_methods.map(payment_method => <PaymentMethodCard payment_method={payment_method}/>)}
            </div>
          </div>
        }
      </div>
    </div>
  )
}

export default UserProfilePage;
