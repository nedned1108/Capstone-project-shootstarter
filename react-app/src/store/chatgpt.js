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
