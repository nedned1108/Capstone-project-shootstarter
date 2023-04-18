const GET_GPT = 'chatgpt/GET_GPT'

const getTheGPT = (gpt) => {
    return {
        type: GET_GPT,
        gpt
    }
}

export const getGPT = () => async (dispatch) => {
    const res = await fetch('/api/gpt/key')
    if (res.ok) {

        const data = await res.json()

        dispatch(getTheGPT(data.gptAPIKey))
        return "Got the GPT"
    }
    return "Could not get the GPT"
}

const initialState = {}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GET_GPT:
            return { key: action.gpt }
        default:
            return state
    }
}
