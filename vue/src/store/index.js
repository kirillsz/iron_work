import { createStore } from 'vuex'


import * as getters from './getters'
import * as mutations from './mutations'
import * as actions from './actions'




export default createStore({

  state: {
    domain: window.location.hostname == "localhost" ? "http://localhost" : "",

    pop_up: false,

  },

  getters,
  mutations,
  actions,

})