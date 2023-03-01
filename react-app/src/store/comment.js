const LOAD_ALLCOMMENTS = 'pledge/LOAD_ALLCOMMENTS';
const ADD_COMMENT = 'pledge/ADD_COMMENT';
const UPDATE_COMMENT = 'pledge/UPDATE_COMMENT';
const DELETE_COMMENT = 'pledge/DELETE_COMMENT';

// Action
export const loadAllComments = (comments) => {
  return {
    type: LOAD_ALLCOMMENTS,
    payload: comments
  }
};

export const addComment = (comment) => {
  return {
    type: ADD_COMMENT,
    payload: comment
  }
};

export const updateComment = (comment) => {
  return {
    type: UPDATE_COMMENT,
    payload: comment
  }
};

export const deleteComment = (id) => {
  return {
    type: DELETE_COMMENT,
    payload: id
  }
};

// Thunk
export const thunkLoadAllComments = () => async (dispatch) => {
  const response = await fetch('/api/comment/');

  if (response.ok) {
    const data = await response.json();
    dispatch(loadAllComments(data.comments))
  }
};

export const thunkCreateComment = (comment) => async (dispatch) => {
  const response  = await fetch(`/api/comment/`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(comment)
  });

  if (response.ok) {
    const comment = await response.json();
    dispatch(addComment(comment))
    return comment
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};

export const thunkUpdateComment = (data) => async (dispatch) => {
  const response = await fetch(`/api/comment/${data.id}`, {
    method: "PUT",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  if (response.ok) {
    const comment = await response.json();
    dispatch(updateComment(comment))
    return comment;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};


export const thunkDeleteComment = (id) => async (dispatch) => {
  const response = await fetch(`/api/comment/${id}`, {
    method: "DELETE"
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(deleteComment(id))
    return data;
  }
};

// InitialState
const initialState = {
  comments: {}
};

// Reducer
const commentReducer = (state = initialState, action) => {
  let newState = { ...state };
  switch (action.type) {
    case LOAD_ALLCOMMENTS:
      newState.comments = normalize(action.payload)
      return newState;
    case ADD_COMMENT:
      newState.comments = {...state.comments, [action.payload.id]: action.payload}
      return newState;
    case UPDATE_COMMENT:
      newState.comments = {...state.comments, [action.payload.id]: action.payload}
      return newState;
    case DELETE_COMMENT:
      newState.comments = {...state.comments}
      delete newState.comments[action.payload]
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

export default commentReducer;
