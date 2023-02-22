import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { thunkLoadAllPledges } from "../../store/pledge";


const PledgePage = () => {
  const dispatch = useDispatch();
  const allPledgesData = useSelector(state => state.pledge.pledges)
  let pledges;
  if (allPledgesData) pledges = Object.values(allPledgesData);
  useEffect(() => {
    dispatch(thunkLoadAllPledges())
  }, [dispatch])

  if (pledges.length == 0) {
    return null
  }

  return (
    <h1>PledgePage</h1>
  )
};

export default PledgePage;
