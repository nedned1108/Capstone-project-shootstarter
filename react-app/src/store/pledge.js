const LOAD_ALLPLEDGES = 'pledge/LOAD_ALLPLEDGES';
const ADD_PLEDGE = 'pledge/ADD_PLEDGE';
const UPDATE_PLEDGE = 'pledge/UPDATE_PLEDGE';
const DELETE_PLEDGE = 'pledge/DELETE_PLEDGE';

// Action
export const loadAllPledges = (pledges) => {
  return {
    type: LOAD_ALLPLEDGES,
    payload: pledges
  }
};

export const addPledge = (pledge) => {
  return {
    type: ADD_PLEDGE,
    payload: pledge
  }
};

export const updatePledge = (pledge) => {
  return {
    type: UPDATE_PLEDGE,
    payload: pledge
  }
};

export const deletePledge = (id) => {
  return {
    type: DELETE_PLEDGE,
    payload: id
  }
};

// Thunk
export const thunkLoadAllPledges = () => async (dispatch) => {
  const response = await fetch('/api/pledge/');

  if (response.ok) {
    const data = await response.json();
    console.log(data)
    dispatch(loadAllPledges(data.pledges))
  }
};

export const thunkCreatePledge = (pledge) => async (dispatch) => {
  console.log(pledge, 'pledgeeeeeeeeeeeeeeeee')
  const response  = await fetch(`/api/project/${pledge.project_id}/pledges`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(pledge)
  });

  if (response.ok) {
    const pledge = await response.json();
    dispatch(addPledge(pledge))
    return pledge
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};

export const thunkUpdatePledge = (data) => async (dispatch) => {
  const response = await fetch(`/api/pledge/${data.id}`, {
    method: "PUT",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  if (response.ok) {
    const pledge = await response.json();
    dispatch(updatePledge(pledge))
    return pledge;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};


export const thunkDeletePledge = (id) => async (dispatch) => {
  const response = await fetch(`/api/pledge/${id}`, {
    method: "DELETE"
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(deletePledge(id))
    return data;
  }
};

// InitialState
const initialState = {
  pledges: {}
};

// Reducer
const pledgeReducer = (state = initialState, action) => {
  let newState = { ...state };
  switch (action.type) {
    case LOAD_ALLPLEDGES:
      newState.pledges = normalize(action.payload)
      return newState;
    case ADD_PLEDGE:
      newState.pledges = {...state.pledges, [action.payload.id]: action.payload}
      return newState;
    case UPDATE_PLEDGE:
      newState.pledges = {...state.pledges, [action.payload.id]: action.payload}
      return newState;
    case DELETE_PLEDGE:
      newState.pledges = {...state.pledges}
      delete newState.pledges[action.payload]
      return newState;
    default:
      return state;
  }
};

// Helper
const normalize = (array) => {
  const obj = {}
  array.forEach((el) => {
    obj[el.id] = el
  });
  return obj;
}

export default pledgeReducer;
