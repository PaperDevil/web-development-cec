<template>
  <div id="app">
    <TodoList />
  </div>
</template>

<script>
import Todo from "./components/Todo";

export default {
  name: "App",
  components: {
    TodoList: Todo,
  },
};
</script>
