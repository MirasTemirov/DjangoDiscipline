export default {
  namespaced: true,
  state: {
    user: null,
    token: null,
  },
  mutations: {
    setEmail(state, payload) {
      if (state.user && "email" in state.user) {
        state.user.email = payload;
      }
    },
    setFirstName(state, payload) {
      if (state.user && "first_name" in state.user) {
        state.user["first_name"] = payload;
      }
    },
    setLastName(state, payload) {
      if (state.user && "last_name" in state.user) {
        state.user["last_name"] = payload;
      }
    },
    setPassword(state, payload) {
      if (state.user && "password" in state.user) {
        state.user["password"] = payload;
      }
    },
    setUser(state, payload) {
      state.user = payload;
    },
    setToken(state, payload) {
      state.token = payload;
    },
    deleteUser(state) {
      state.user = null;
    },
    deleteToken(state) {
      state.token = null;
    },
  },
  actions: {
    setEmail({ commit }, payload) {
      commit("setEmail", payload);
    },
    setFirstName({ commit }, payload) {
      commit("setFirstName", payload);
    },
    setLastName({ commit }, payload) {
      commit("setLastName", payload);
    },
    setPassword({ commit }, payload) {
      commit("setPassword", payload);
    },
    setUser({ commit }, payload) {
      commit("setUser", payload);
    },
    setToken({ commit }, payload) {
      commit("setToken", payload);
    },
    logoutUser({ commit }) {
      commit("deleteToken");
      commit("deleteUser");
    },
  },
  getters: {
    user(state) {
      return state.user;
    },
    token(state) {
      return state.token;
    },
  },
};
