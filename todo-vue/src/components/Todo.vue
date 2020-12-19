<template>
  <div class="">
    <label for="input-2x">TODO :</label>
    <input
      type="text"
      name="input-2x"
      v-model="input"
      placeholder="Что ты хочешь сделать?"
    />
    <input type="button" @click="addTodo()" value="Добавить" />
    <input type="checkbox" v-model="showDelete" />
    <input type="checkbox" v-model="hideComplete" />
    <hr />
    <div class="" v-for="todo in todos" :key="todo">
      <TodoItem
        :msg="todo.text"
        :showDelete="showDelete"
        :hideComplete="hideComplete"
      />
    </div>
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
        fetch(this.API_URL, {
          method: 'POST',
          body: JSON.stringify({ text }),
          headers: {
            'Content-Type': 'application/json'
          },
        })

        console.log(`Мы нажали кнопку "Добавить" при тексте ${this.input}`);
      }
    },
    updateList() {

      console.log(this.todo)

      console.log('Start updating')
      fetch(this.API_URL, {
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
    setInterval(this.updateList, 2000)
  }
};
</script>

<style scoped>
</style>