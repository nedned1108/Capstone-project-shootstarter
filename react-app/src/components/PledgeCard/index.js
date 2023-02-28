import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useHistory } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import UpdatePledgeModal from "../UpdatePledgeModal";
import { thunkDeletePledge, thunkChoosePledge } from "../../store/pledge";
import { authenticate } from "../../store/session";
import { useModal } from "../../context/Modal";
import ThankYouModal from "./ThankYouModal";
import ChooseOtherModal from "./ChooseOtherModal";
import ConfirmDeletePledge from "./ConfirmDeletePledge";
import './PledgeCard.css'


const PledgeCard = ({ pledge }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const currentUser = useSelector(state => state.session.user)
  const { setModalContent } = useModal()

  const deletePledge = (e) => {
    return dispatch(thunkDeletePledge(e))
  } 
  const choosePledge = async (e) => {
    e.preventDefault();

    const choice = {
      user_id: currentUser.id,
      pledge_id: pledge.id,
      project_id: pledge.project_id
    };
    if (currentUser.pledges.includes(pledge.id)) {
      setModalContent(<ChooseOtherModal />)
    } else {
      const data = await dispatch(thunkChoosePledge(choice))
      setModalContent(<ThankYouModal />)
      dispatch(authenticate())
    }
  }

  if (!pledge) {
    return null
  }

  return (
    <div className="pledgeCardMainDiv">
      <div className="price_reward">
        <h4>
          Pledge ${pledge.price}
        </h4>
        <h4>
          {pledge.pledge_name}
        </h4>
        <p>
          {pledge.rewards}
        </p>
      </div>
      <div className="delivery">
        <p>ESTIMATED DELIVERY</p>
        <h6>{pledge.estimated_delivery}</h6>
        <p>Ships to</p>
        <h6>{pledge.ships_to}</h6>
        {currentUser && pledge.owner_id == currentUser.id && 
          <div className="update_delete">
            <OpenModalButton 
              buttonText='Update Pledge'
              modalComponent={<UpdatePledgeModal pledge={pledge} />}
            />
            <OpenModalButton 
              buttonText="Delete Pledge"
              modalComponent={<ConfirmDeletePledge pledge={pledge} />}
            />
          </div> 
        }
        {currentUser && pledge.owner_id != currentUser.id && 
          <button onClick={choosePledge} >Choose this reward</button>
        }
      </div>
    </div>
  )
}

export default PledgeCard;
