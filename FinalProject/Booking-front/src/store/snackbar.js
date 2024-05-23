export default {
  namespaced: true,
  state: {
    status: false,
    text: "",
  },
  mutations: {
    setStatus(state, payload) {
      state.status = payload;
    },
    setText(state, payload) {
      state.text = payload;
    },
  },
  actions: {
    setStatus({ commit }, payload) {
      commit("setStatus", payload);
    },
    setText({ commit }, payload) {
      commit("setText", payload);
    },
  },
  getters: {
    status(state) {
      return state.status;
    },
    text(state) {
      return state.text;
    },
  },
};
