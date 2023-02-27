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
