const LOAD_ALLPROJECTS = 'project/LOAD_ALLPROJECTS';
const ADD_PROJECT = 'project/ADD_PROJECT';
const UPDATE_PROJECT = 'project/UPDATE_PROJECT';
const DELETE_PROJECT = 'project/DELETE_PROJECT';

// Action
export const loadAllProjects = (projects) => {
  return {
    type: LOAD_ALLPROJECTS,
    payload: projects
  }
};

export const addProject = (project) => {
  return {
    type: ADD_PROJECT,
    payload: project
  }
};

export const updateProject = (project) => {
  return {
    type: UPDATE_PROJECT,
    payload: project
  }
};

export const deleteProject = (id) => {
  return {
    type: DELETE_PROJECT,
    payload: id
  }
};

// Thunk
export const thunkLoadAllProjects = () => async (dispatch) => {
  const response = await fetch('/api/project/');

  if (response.ok) {
    const data = await response.json();
    dispatch(loadAllProjects(data.projects))
  }
};


export const thunkCreateProject = (project) => async (dispatch) => {
  const response  = await fetch(`/api/project/`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(project)
  });

  if (response.ok) {
    const project = await response.json();
    dispatch(addProject(project))
    return project
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};


export const thunkUpdateProject = (data) => async (dispatch) => {
  const response = await fetch(`/api/project/${data.id}`, {
    method: "PUT",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  if (response.ok) {
    const project = await response.json();
    dispatch(updateProject(project))
    return project;
  } else {
    const data = await response.json();
    if (data.errors) {
      return data
    }
  }
};


export const thunkDeleteProject = (id) => async (dispatch) => {
  const response = await fetch(`/api/project/${id}`, {
    method: "DELETE"
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(deleteProject(id))
    return data;
  }
};

// InitialState
const initialState = {
  projects: {}
};

// Reducer
const projectReducer = (state = initialState, action) => {
  let newState = { ...state };
  switch (action.type) {
    case LOAD_ALLPROJECTS:
      newState.projects = normalize(action.payload)
      return newState;
    case ADD_PROJECT:
      newState.projects = {...state.projects, [action.payload.id]: action.payload}
      return newState;
    case UPDATE_PROJECT:
      newState.projects = {...state.projects, [action.payload.id]: action.payload}
      return newState;
    case DELETE_PROJECT:
      newState.projects = {...state.projects}
      delete newState.projects[action.payload]
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

export default projectReducer;
