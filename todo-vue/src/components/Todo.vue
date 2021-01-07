<template>
  <div class="header">
    <!-- Header -->
    <h1>Todo List</h1>
    <input
      type="text"
      name="input-2x"
      v-model="input"
      placeholder="Что ты хочешь сделать?"
      class="fs-3 text m-2"
    />
    <input class="btn-success mx-2" type="button" @click="addTodo()" value="Добавить" />
    <div class="controls">
      <div class="my-1">
        <input type="checkbox" id="checkbox-1" v-model="showDelete" />
        <label for="checkbox-1">Show Delete</label>
      </div>
      <div class="my-1">
        <input type="checkbox" id="checkbox-2" v-model="hideComplete" />
        <label for="checkbox-2">Hide Complete</label>
      </div>
    </div>
    <hr />
    <!-- End Header -->

    <!-- Todo List -->
    <div class="" v-for="todo in todos" :key="todo">
      <TodoItem
        :id="todo.id"
        :msg="todo.text"
        :isComplete="todo.is_complete"
        :isDelete="todo.is_delete"
        :showDelete="showDelete"
        :hideComplete="hideComplete"
      />
    </div>
    <!-- End Todo List -->
  </div>
</template>

<script>
import TodoItem from "./TodoItem";

export default {
  components: {
    TodoItem,
  },
  data: function () {
    return {
      todos: [],
      input: "",
      showDelete: false,
      hideComplete: false,
      API_URL: 'http://127.0.0.1:5000/',
    };
  },
  methods: {
    addTodo() {
      if (this.input) {
        let text = this.input;
        fetch(this.API_URL + '/create', {
          method: 'POST',
          body: JSON.stringify({ text }),
          headers: {
            'Content-Type': 'application/json'
          },
        })
      }
    },
    updateList() {
      fetch(this.API_URL + '/list', {
        method: 'GET'
      })
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        this.todos = data
        console.log(`Updated with ${data}`)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    setInterval(this.updateList, 600)
  }
};
</script>

<style scoped>
.header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  padding: 5%;
}
.controls {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  text-align: center;

}
</style>