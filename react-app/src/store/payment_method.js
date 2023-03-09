const LOAD_ALLPAYMENTS = 'pledge/LOAD_ALLPAYMENTS';
const ADD_PAYMENT = 'pledge/ADD_PAYMENT';
const UPDATE_PAYMENT = 'pledge/UPDATE_PAYMENT';
const DELETE_PAYMENT = 'pledge/DELETE_PAYMENT';

// Action
export const loadAllPayments = (payments) => {
  return {
    type: LOAD_ALLPAYMENTS,
    payload: payments
  }
};

export const addPayment = (payment) => {
  return {
    type: ADD_PAYMENT,
    payload: payment
  }
};

export const updatePayment = (payment) => {
  return {
    type: UPDATE_PAYMENT,
    payload: payment
  }
};

export const deletePayment = (id) => {
  return {
    type: DELETE_PAYMENT,
    payload: id
  }
};

// Thunk
export const thunkLoadAllPayments = () => async (dispatch) => {
  const response = await fetch('/api/payment/');

  if (response.ok) {
    const data = await response.json();
    dispatch(loadAllPayments(data.payments))
  }
};

export const thunkCreatePayment = (payment) => async (dispatch) => {
  const response  = await fetch(`/api/payment/`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payment)
  });

  if (response.ok) {
    const payment = await response.json();
    dispatch(addPayment(payment))
    return payment
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};

export const thunkUpdatePayment = (data) => async (dispatch) => {
  const response = await fetch(`/api/payment/${data.id}`, {
    method: "PUT",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  if (response.ok) {
    const payment = await response.json();
    dispatch(updatePayment(payment))
    return payment;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};

export const thunkDeletePayment = (id) => async (dispatch) => {
  const response = await fetch(`/api/payment/${id}`, {
    method: "DELETE"
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(deletePayment(id))
    return data;
  }
};

// InitialState
const initialState = {
  payments: {}
};

// Reducer
const paymentReducer = (state = initialState, action) => {
  let newState = { ...state };
  switch (action.type) {
    case LOAD_ALLPAYMENTS:
      newState.payments = normalize(action.payload)
      return newState;
    case ADD_PAYMENT:
      newState.payments = {...state.payments, [action.payload.id]: action.payload}
      return newState;
    case UPDATE_PAYMENT:
      newState.payments = {...state.payments, [action.payload.id]: action.payload}
      return newState;
    case DELETE_PAYMENT:
      newState.payments = {...state.payments}
      delete newState.payments[action.payload]
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

export default paymentReducer;
