<template>
  <div v-if="isDelete">
    <div v-if="showDelete" class="TodoItem" v-show="needToShow">
      <input
        class="input-check"
        type="checkbox"
        name="complete"
        v-model="isComplete"
        @click="setComplete()"
      />
      <h4 v-if="isComplete" style="text-decoration: line-through">{{ msg }}</h4>
      <h4 v-else>{{ msg }}</h4>
      <input class="control-button btn-secondary" type="button" value="Восстановить" @click="deleteOrRetore()" />
    </div>
  </div>
  <div v-else class="TodoItem" v-show="needToShow">
    <input
      class="input-check"
      type="checkbox"
      name="complete"
      v-model="isComplete"
      @click="setComplete()"
    />
    <h4 v-if="isComplete" style="text-decoration: line-through">{{ msg }}</h4>
    <h4 v-else>{{ msg }}</h4>
    <input class="control-button btn-danger" type="button" value="Удалить" @click="deleteOrRetore()" />
  </div>
</template>

<script>
export default {
  name: "TodoItem",
  props: ["id", "msg", "isComplete", "isDelete", "showDelete", "hideComplete"],
  data () {
    return {
      API_URL: 'http://127.0.0.1:5000/'
    }
  },
  methods: {
    deleteOrRetore() {
      fetch(this.API_URL + `/delete/${this.id}`, {
          method: 'DELETE',
          mode: 'same-origin',
          headers: {
            'Content-Type': 'application/json'
          },
        })
    },
    setComplete() {
      fetch(this.API_URL + `/complete/${this.id}`, {
          method: 'POST',
          mode: 'same-origin',
          headers: {
            'Content-Type': 'application/json'
          },
        })  
    }
  },
  computed: {
    needToShow() {
      console.log(this.hideComplete);
      return !(this.isComplete && this.hideComplete);
    },
  },
  created() {
    console.log(this.msg)
  },
};
</script>

<style scoped>
.TodoItem {
  display: flex;
  flex-direction: row;
  text-align: center;
  vertical-align: center;
  justify-content: middle;
  border: 1px solid black;
  padding: 3px;
  margin-bottom: 10px;
}

.input-check {
  margin-top: auto;
  margin-bottom: auto;
  margin-right: 15px;;
}

.control-button {
  margin-left: auto;
}
</style>