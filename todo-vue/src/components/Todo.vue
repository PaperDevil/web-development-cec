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
        :msg="todo"
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
    };
  },
  methods: {
    addTodo() {
      if (this.input) {
        this.todos.push(this.input);
        console.log(`Мы нажали кнопку "Добавить" при тексте ${this.input}`);
      }
    },
  },
};
</script>

<style scoped>
</style>