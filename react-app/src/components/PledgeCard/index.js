import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdatePledgeModal from "../UpdatePledgeModal";
import { thunkDeletePledge } from "../../store/pledge";
import './PledgeCard.css'


const PledgeCard = ({ pledge }) => {
  const dispatch = useDispatch();
  const currentUser = useSelector(state => state.session.user)
  const deletePledge = (e) => {
    return dispatch(thunkDeletePledge(e))
  } 

  if (!pledge) {
    return null
  }

  return (
    <div>
      <div>
        Pledge ${pledge.price}
        {pledge.pledge_name}
        {pledge.rewards}
      </div>
      <div>
        <p>ESTIMATED DELIVERY {pledge.estimated_delivery}</p>
        <p>Ships to {pledge.ships_to}</p>
        {currentUser && pledge.owner_id == currentUser.id && 
          <div>
            <OpenModalButton 
              buttonText='Update Pledge'
              modalComponent={<UpdatePledgeModal pledge={pledge}/>}
            />
            <button onClick={() => deletePledge(pledge.id)}>Delete Pledge</button>
          </div> 
          // : "" 
        }
      </div>
    </div>
  )
}

export default PledgeCard;
